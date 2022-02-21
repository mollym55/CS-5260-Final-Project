
import copy

# The Transform class represents the transform operation
class Transform:
    def __init__(self, state, country, template, multiplier = 1):
        self.state = copy.deepcopy(state)
        self.country = country
        self.template = template
        self.multiplier = multiplier
    
    def execute(self):
        inputs = self.template["in"]
        outputs = self.template["out"]
        for r_type in inputs:
            self.state[self.country][r_type] = self.state[self.country][r_type] - inputs[r_type] * self.multiplier
        for r_type in outputs:
            self.state[self.country][r_type] = self.state[self.country][r_type] + outputs[r_type] * self.multiplier
        return self.state
        
    def toString(self):
        string = "(TRANSFORM " + self.country + " INPUTS ("
        inputs = self.template["in"]
        outputs = self.template["out"]
        for r_type in inputs:
            string = string + "(" + r_type + " " + str(inputs[r_type] * self.multiplier) + ")"
        string = string + ") OUTPUTS("
        for r_type in outputs:
            string = string + "(" + r_type + " " + str(outputs[r_type] * self.multiplier)+ ")"
        string = string + "))"
        #below is for p2 wrapper purposes
        string = string + " || "
        for r_type in inputs:
            string = string + " " + r_type + " " + str(inputs[r_type])
        string = string + " || "
        for r_type in outputs:
            string = string + " " + r_type + " " + str(outputs[r_type])
        string = string + " || "
        string = string + str(self.multiplier)
        return string
