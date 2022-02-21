
import copy

# The Transfer class transfers resources from one country to another country
class Transfer:
    def __init__(self, state, recieve, deliver, trade):
        self.state = copy.deepcopy(state)
        self.recieve = recieve
        self.deliver = deliver
        self.trade = trade

    def execute(self):
        resource = self.trade[0]
        quantity = self.trade[1]
        self.state[self.recieve][resource] = self.state[self.recieve][resource] - quantity #deduct quantity of resource from country
        self.state[self.deliver][resource] = self.state[self.deliver][resource] + quantity #increase quantity of resource to the other country
        return self.state

    def toString(self):
        resource = self.trade[0]
        quantity = self.trade[1]
        string = "(TRANSFER FROM " + self.recieve + " TO " + \
            self.deliver + " (" + resource + " " + str(quantity) + "))"
        return string

    def isRecievedFrom(self):
        return self.recieve

    def isDeliveredTo(self):
        return self.deliver
