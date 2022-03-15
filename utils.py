import pandas as pd
from transform import Transform
from transfer import Transfer
from belongings import comfort
import numpy as np
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

# calculate_transform_max_multiplier calculates max resource country can apply
def calculate_transform_max_multiplier(resources, template):
    multiplier = -1
    inputs = template["in"]
    population = resources["R1"]
    for res in inputs:
        if res in comfort.keys():

            available = resources[res] - \
                int(comfort[res] * population * 0.2)

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

# logistic is the sigmoid function
def logistic(payout, k, L):
    return L / (1 + np.exp(-k * payout))

# calculate_success_probability calculates success rate of country
def calculate_success_probability(myCountry, currentState, nextState, action, resourcePath):
    
    if isInstance(action, Transfer):
        recievedCountry = action.isRecievedFrom()
        deliveredCountry = action.isDeliveredTo()
        other = ""
        if recievedCountry != myCountry:
            other = recievedCountry
        else:
            other = deliveredCountry
        payout = calculate_state_quality(nextState, other, resourcePath) - calculate_state_quality(currentState, other, resourcePath)
        return logistic(payout, 1, 1)
   
    if isinstance(action, Transform):
        return 1

# calculate_state_quality calculates state quality of country
def calculate_state_quality(state, country, path):
    country_resources = state[country]
    population = country_resources["R1"]
    comfortable = {}
    for resource in comfort.keys():
        comfortable[resource] = int(comfort[resource] * population)

    resources_df = pd.read_excel(path)
    weighted_sum = 0.0
    resource_quantity = country_resources[resource]
    resource_value = resources_df[resources_df['Resource']
                                      == resource]['Weight'].iloc[0]
    difference = resource_quantity - comfortable[resource]
    weighted_sum = weighted_sum + \
               (comfortable[resource] * resource_value) + \
               (difference * resource_value / 2)

    normalized = weighted_sum / population
    
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
    # Can't trade population or waste
    untradeable = ['R1', "R21'", "R22'", "R23'"]
    demand = {}
    
    # create a list of demand for each country based on belongings
    for country in state:
        resources = state[country]
        population = resources["R1"]
        demand[country] = {}
        for res in comfort:
            if res not in untradeable:
                if resources[res] - int(comfort[res] * population) < 0:
                    demand[country][res] = int(
                        comfort[res] * population) - resources[res]
                if resources[res] - int(comfort[res] * population * 0.2) < 0:
                    demand[country][res] = int(
                        comfort[res] * population * 0.2) - resources[res]
    trades = []
    # generate imports based on demand
    for res in demand[myCountry]:
        myDemand = demand[myCountry][res]
        for country in countryList:
            if country != myCountry:
                if state[country][res] != 0:
       
                    theirQuantity = int(state[country][res] / 5) if state[country][res] <= int(comfort[res] * state[country]
                                                                                                   ["R1"] * 0.2) else state[country][res] - int(comfort[res] * state[country]["R1"] * 0.2)
                    amount = myDemand if myDemand < theirQuantity else theirQuantity
                    if amount == 0:
                        continue
                    content = (res, amount)
                    importTrade = Transfer(state, country, myCountry, content)
                    trades.append(importTrade)

    # generate exports based on demands
    for country in demand:
        if country != myCountry:
            for res in demand[country]:
                theirDemand = demand[country][res]
     
                if res not in demand[myCountry]:
                    mySupply = state[myCountry][res] - \
                        int(comfort[res] *
                            state[myCountry]["R1"] * 0.2)
                    amount = theirDemand if theirDemand < mySupply else mySupply
                    if amount == 0:
                        continue
                    content = (res, amount)
                    exportTrade = Transfer(state, myCountry, country, content)
                    trades.append(exportTrade)

    return trades

# write_to_file writes schedule to file
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
