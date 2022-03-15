from random import uniform
import copy

# Belongings Class represents the levels of the resources 

comfort = {'R2': 3, 'R3': 5, 'R4': 2, 'R21': 1.2, 'R22': 2, 'R23': 3}

class Belongings:
    def __init__(self, state, country):
        self.state = copy.deepcopy(state)
        self.country = country 
        self.resources = self.state[self.country]
        self.population = self.resources["R1"]
        self.percentages = {}

        self.levels = {}
        for res in comfort:
            self.levels[res] = self.population * comfort[res]
        self.percentages = self.generate_percentages()

    # checks if a country can transform quantity of resource
    def is_valid_transfer(self, resource, quantity):
        return (self.resources[resource] - quantity) > 0

    def get_population(self):
        return self.population

    def get_resources(self):
        resources = {}
        for res in self.resources:
            if res in self.percentages:
                resources[res] = self.resources[res]
        return resources

    def get_percentages(self):
        return self.percentages
    
    def get_levels(self):
        return self.levels

    def generate_percentages(self):
        for resource in self.levels:
            self.percentages[resource] = self.resources[resource] / self.levels[resource]
        return self.percentages 
    
