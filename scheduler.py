import heapq
import copy

# The Partial class represents partial schedule
class Partial:
  
    # __init__ constructs Partial object
    def __init__(self, expectedUtility, state, schedule):
        self.expectedUtility = expectedUtility
        self.state = state
        self.schedule = schedule
    
    # getExpectedUtility returns expected utility
    def getExpectedUtility(self):
        return self.expectedUtility
    
    # getState returns state of countries
    def getState(self):
        return self.state
    
    # getSchedule returns schedule
    def getSchedule(self):
        return self.schedule
    
    # __lessthan__ represents < operator
    def __lessthan__(self, other):
        if isinstance(other, Partial):
            if self.expectedUtility == other.expectedUtility:
                return len(self.schedule) > len(other.schedule)
            else:
                return self.expectedUtility < other.expectedUtility
        else:
            return False
          
    # __lessequal__ represents <= operator
    def __lessequal__(self, other):
        if isinstance(other, Partial):
            return self.expectedUtility <= other.expectedUtility
        else:
            return False

# The Scheduler class is the research algorithm
class Scheduler:
  
    # __init__ constructs Scheduler object
    def __init__(self, countries):
        self.countries = countries
    
    # search searches for the best schedule
    def search(self, maxDepth, maxSize):
        part = []
        visited = []
        results = []
        stateStatus = self.countries.getStateStatus()
        partial = Partial(0, stateStatus, [])
        heapq.heappush(part, partial)
        while part:
            curr = heapq.heappop(part)
            state = curr.getState()
            schedule = curr.getSchedule()
            
            if len(schedule) == maxDepth:
                heapq.heappush(results, curr)
           
            else:
                if state not in visited:
                    visited.append(state) #populates state in visited array

                    for successor in self.countries.getSuccessors(state):
                        nextState = successor[0]
                        nextAction = successor[1]
                        nextExpectedUtility = self.countries.getExpectedUtility(state, nextState, len(schedule) + 1, nextAction)
                        nextSchedule = schedule + [[nextAction.toString(), nextExpectedUtility]]
                        nextItem = Partial(-1 * nextExpectedUtility, nextState,
                                        copy.deepcopy(nextSchedule))
                        if nextState not in visited:
                            heapq.heappush(part, nextItem)
                       
                            if len(part) > maxSize:
                                part.pop()
        return results
