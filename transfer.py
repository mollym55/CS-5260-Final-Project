
import copy

# The Transfer class represents the singleton transfer operation
class Transfer:
    def __init__(self, state, recieve, deliver, trade):
        self.state = copy.deepcopy(state)
        self.recieve = recieve
        self.deliver = deliver
        self.trade = trade

    def execute(self):
        resource = self.trade[0]
        quantity = self.trade[1]
        self.state[self.recieve][resource] = self.state[self.recieve][resource] - quantity
        self.state[self.deliver][resource] = self.state[self.deliver][resource] + quantity
        return self.state

    def toString(self):
        resource = self.trade[0]
        quantity = self.trade[1]
        string = "(TRANSFER FROM " + self.recieve + " TO " + \
            self.deliver + " (" + resource + " " + str(quantity) + "))"
        return string

    def isFrom(self):
        return self.recieve

    def isTo(self):
        return self.deliver
