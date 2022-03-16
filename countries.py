import pandas as pd
from transform import Transform
import utils

# Countries Class calculates the expected utility to a country of a schedule
class Countries:
  
    # __init___ constructs Countries object
    def __init__(self, myCountry, transform_resources, initStatePath, resourcePath):
        self.myCountry = myCountry
        self.transform_resources = transform_resources
        self.resourcePath = resourcePath
        data = pd.read_excel(initStatePath)
        df = pd.DataFrame(data)
        initialStates = {}
        for index, row in df.iterrows():
            initialStates[row["Country"]] = {}
            initialStates[row["Country"]]["R1"] = row["R1"]
            initialStates[row["Country"]]["R2"] = row["R2"]
            initialStates[row["Country"]]["R3"] = row["R3"]
            initialStates[row["Country"]]["R4"] = row["R4"]
            initialStates[row["Country"]]["R21"] = row["R21"]
            initialStates[row["Country"]]["R22"] = row["R22"]
            initialStates[row["Country"]]["R23"] = row["R23"]
            initialStates[row["Country"]]["R1'"] = row["R1'"]
            initialStates[row["Country"]]["R21'"] = row["R21'"]
            initialStates[row["Country"]]["R22'"] = row["R22'"]
            initialStates[row["Country"]]["R23'"] = row["R23'"]
        self.stateStatus = initialStates
    
    # getStateStatus returns intitial status of the countries
    def getStateStatus(self):
        return self.stateStatus

    # getSuccessors generates successors
    def getSuccessors(self, state):
        successors = []
        myResources = state[self.myCountry]
        for res in self.transform_resources:
            maxMult = utils.calculate_transform_max_multiplier(
                myResources, res)
            if maxMult:
                transformation = Transform(
                    state, self.myCountry, res, maxMult)
                successors.append([transformation.execute(), transformation])
                
        trades = utils.generate_trades(state, self.myCountry)
        for trade in trades:
            successors.append([trade.execute(), trade])
        return successors
    
    # getExpectedUtility calculates EU to a country of a schedule
    def getExpectedUtility(self, currentState, nextState, length, action):
        startQuality = utils.calculate_state_quality(self.stateStatus, self.myCountry, self.resourcePath)
        endQuality = utils.calculate_state_quality(nextState, self.myCountry, self.resourcePath)
        gamma = 0.99
        reward = endQuality - startQuality
        discountedReward = (gamma ** length) * reward
        probabilitySuccess = utils.calculate_success_probability(
            self.myCountry, currentState, nextState, action, self.resourcePath)
        failure_cost = -discountedReward * -1
        eu = probabilitySuccess * discountedReward + \
            (1 - probabilitySuccess) * failure_cost
        return eu
