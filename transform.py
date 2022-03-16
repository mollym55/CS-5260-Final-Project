import copy

# The Transform class represents TRANSFORMations that happen between countries
class Transform:
    
    # __init___ constructs Transform object
    def __init__(self, state, country, resources, multiplier = 1):
        self.state = copy.deepcopy(state)
        self.country = country
        self.resources = resources
        self.multiplier = multiplier
    
    def execute(self):
        inputs = self.resources["in"]
        outputs = self.resources["out"]
        for res in inputs:
            self.state[self.country][res] = self.state[self.country][res] - inputs[res] * self.multiplier
        for res in outputs:
            self.state[self.country][res] = self.state[self.country][res] + outputs[res] * self.multiplier
        return self.state
        
    def toString(self):
        string = "(Transfrom " + self.country + " inputs ("
        inputs = self.resources["in"]
        outputs = self.resources["out"]
        for res in inputs:
            string = string + "(" + res + " " + str(inputs[res] * self.multiplier) + ")"
        string = string + ") OUTPUTS("
        for res in outputs:
            string = string + "(" + res + " " + str(outputs[res] * self.multiplier)+ ")"
        string = string + "))"
        string = string + str(self.multiplier)
        return string
