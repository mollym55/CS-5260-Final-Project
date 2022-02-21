
import copy

# The Transform class represents TRANSFORMations that happen between countries
class Transform:
    def __init__(self, state, country, resources, multiplier = 1):
        self.state = copy.deepcopy(state)
        self.country = country
        self.resources = resources
        self.multiplier = multiplier
    
    def execute(self):
        inputs = self.resources["input"]
        outputs = self.resources["output"]
        for r_type in inputs:
            self.state[self.country][r_type] = self.state[self.country][r_type] - inputs[r_type] * self.multiplier
        for r_type in outputs:
            self.state[self.country][r_type] = self.state[self.country][r_type] + outputs[r_type] * self.multiplier
        return self.state
        
    def toString(self):
        string = "(TRANSFORM " + self.country + " INPUTS ("
        inputs = self.resources["input"]
        outputs = self.resources["output"]
        for r_type in inputs:
            string = string + "(" + r_type + " " + str(inputs[r_type] * self.multiplier) + ")"
        string = string + ") OUTPUTS("
        for r_type in outputs:
            string = string + "(" + r_type + " " + str(outputs[r_type] * self.multiplier)+ ")"
        string = string + "))"
        string = string + str(self.multiplier)
        return string
