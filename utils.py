import pandas as pd
from transform import Transform
from transfer import Transfer
import numpy as np
from thresholds import comfortable_level
import os

# getInitialState returns JSON formatted file
def getInitialState(fileName, rowName):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    myFile = os.path.join(THIS_FOLDER, fileName)
    df = pd.read_excel(myFile)
    df.set_index("Country", inplace = True)
    row = df.loc[rowName]
    initialStates = {}
    initialStates["R1"] = row["R1"]
    initialStates["R2"] = row["R2"]
    initialStates["R3"] = row["R3"]
    initialStates["R4"] = row["R4"]
    initialStates["R21"] = row["R21"]
    initialStates["R22"] = row["R22"]
    initialStates["R23"] = row["R23"]
    initialStates["R1'"] = row["R1'"]
    initialStates["R21'"] = row["R21'"]
    initialStates["R22'"] = row["R22'"]
    initialStates["R23'"] = row["R23'"]
    return initialStates

# calculate_transform_max_multiplier
# this calculates the max amount of a given transform template that can be applied
# to a country given their resources
# @resources(dict): a list of resources with their corresponding quantity
# @template(dict): a transform template


def calculate_transform_max_multiplier(resources, template):
    multiplier = -1
    inputs = template["in"]
    population = resources["R1"]
    for res in inputs:
   
            available = resources[res] - \
                int(population * 0.2)
           
            if available > 0:
                if multiplier == -1:
                    multiplier = int(available / inputs[res])
                else:
                    multiplier = min(multiplier, int(
                        available / inputs[res]))
            else:
                multiplier = 0
        else:
            if multiplier == -1:
                multiplier = int(resources[res] / inputs[res])
            else:
                multiplier = min(multiplier, int(
                    resources[res] / inputs[res]))
    return multiplier

# logistic
# this is the sigmoid function
# @payout(int): the payout of a transfer operation which acts as the x param
# @k(int): param k as seen in the sigmoid function definition
# @L(int): param L as seen in the sigmoid function definition


def logistic(payout, k, L):
    return L / (1 + np.exp(-k * payout))

# calculate_success_probability
# this calculates the success rate of a given action based on the current world state
# @myCountry(str): the name of our country
# @curState(dict): the current world state
# @nextState(dict): the world state after executing the given action
# @actioon(obk): a transfer or transform operation
# @resourceWeightPath(str): the path to the resource weight file


def calculate_success_probability(myCountry, currentState, nextState, action, resourcePath):
    # if the action is transfer, the success rate is calculated based on the payout
    # with respect to the other country
    if isInstance(action, Transfer):
        fromCountry = action.isRecievedFrom()
        toCountry = action.isDeliveredTo()
        other = ""
        if fromCountry != myCountry:
            other = fromCountry
        else:
            other = toCountry
        payout = calculate_state_quality(nextState, other, resourcePath) - 
                      calculate_state_quality(currentState, other, resourcePath)
        return logistic(payout, 1, 1)
   
    if isinstance(action, Transform):
        return 1

# calculate_state_quality
# this calculates the state quality for a given country in the given world state
# @state(dict): the world state
# @country(str): the name of our country
# @path(str): the path to the weight file


def calculate_state_quality(state, country, path):
    country_resources = state[country]
    population = country_resources["R1"]

    # Calculate required amounts of resources for "survival" and "comfortable" level
    survival = {}
    comfortable = {}
    for resource in comfortable_level.keys():
        survival[resource] = int(
            comfortable_level[resource] * 0.2 * population)
        comfortable[resource] = int(comfortable_level[resource] * population)

    # print(survival)
    # print(comfortable)

    resources_df = pd.read_excel(path)
    weighted_sum = 0.0
    below_survival = False

    for resource in country_resources.keys():
        resource_quantity = country_resources[resource]
        resource_value = resources_df[resources_df['Resources']
                                      == resource]['Weight'].iloc[0]
        above_comfortable = False

        if resource in comfortable.keys():
            if resource_quantity < int(survival[resource]):
                below_survival = True
            elif resource_quantity >= int(comfortable[resource]):
                above_comfortable = True

        if above_comfortable:
            difference = resource_quantity - comfortable[resource]
            weighted_sum = weighted_sum + \
                (comfortable[resource] * resource_value) + \
                (difference * resource_value / 2)
        else:
            weighted_sum = weighted_sum + (resource_quantity * resource_value)

    normalized = weighted_sum / population
    if below_survival:
        return normalized - 1000
    else:
        return normalized

# generate_trades
# this generates a list of economical transfer operations for myCountry at the given state
# we define an "economical transfer" for part 1 to be:
# a) importing resources that we need
# b) exporting resources that we have in extra
# @state(dict): the world state
# @myCountry(str): the name of our country


def generate_trades(state, myCountry):
    countryList = state.keys()
    # list of resources and wastes that are impractical for trading, at least for part 1
    untradeable_resources = ['R1', 'R4', 'R7', 'R19', 'R21', 'R22',
                             "R1'", "R5'", "R6'", "R18'", "R19'", "R20'", "R21'", "R22'"]
    demand = {}
    # create a list of demand for each country based on thresholds
    for country in state:
        resources = state[country]
        population = resources["R1"]
        demand[country] = {}
        for r_type in comfortable_level:
            if r_type not in untradeable_resources:
                if resources[r_type] - int(comfortable_level[r_type] * population) < 0:
                    demand[country][r_type] = int(
                        comfortable_level[r_type] * population) - resources[r_type]
                if resources[r_type] - int(comfortable_level[r_type] * population * 0.2) < 0:
                    demand[country][r_type] = int(
                        comfortable_level[r_type] * population * 0.2) - resources[r_type]
    #print("demands: ", demand)

    trades = []
    # generate imports based on our demand
    for r_type in demand[myCountry]:
        myDemand = demand[myCountry][r_type]
        for country in countryList:
            if country != myCountry:
                if state[country][r_type] != 0:
                    # we force all countries to trade with us for part 1 even if
                    # the resource that we want is below their survival level.
                    # Although if that is the case, the amount that they are
                    # willing to give us is 20% of what they have
                    theirSupply = int(state[country][r_type] / 5) if state[country][r_type] <= int(comfortable_level[r_type] * state[country]
                                                                                                   ["R1"] * 0.2) else state[country][r_type] - int(comfortable_level[r_type] * state[country]["R1"] * 0.2)
                    amount = myDemand if myDemand < theirSupply else theirSupply
                    if amount == 0:
                        continue
                    content = (r_type, amount)
                    importTrade = Transfer(state, country, myCountry, content)
                    trades.append(importTrade)

    # generate exports based on others' demand
    for country in demand:
        if country != myCountry:
            for r_type in demand[country]:
                theirDemand = demand[country][r_type]
                # we do not want our country to export resources that it is already
                # in shortage of for part 1
                if r_type not in demand[myCountry]:
                    mySupply = state[myCountry][r_type] - \
                        int(comfortable_level[r_type] *
                            state[myCountry]["R1"] * 0.2)
                    amount = theirDemand if theirDemand < mySupply else mySupply
                    if amount == 0:
                        continue
                    content = (r_type, amount)
                    exportTrade = Transfer(state, myCountry, country, content)
                    trades.append(exportTrade)

    return trades

# write_to_file
# this writes the schedule to the given output file
# @path(str): the path to the output file
# @schedule(list): the schedule

def write_to_file(path, schedule, schedule_num):
    output_file = open(path, "a")
    output_file.write("Schedule " + str(schedule_num) + "\n")
    for step in schedule:
        action = step[0]
        eu = step[1]
        line = str(action) + " EU: " + str(eu)
        print(line)
        output_file.write(line)
        output_file.write("\n")
    output_file.write("\n")
    output_file.close()
