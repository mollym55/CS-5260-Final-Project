import heapq
import copy

# # The Part class represents partial schedule
class Part:
  
    # __init__ contructs Part object
    def __init__(self, expectedUtility, state, partial):
        self.expectedUtility = expectedUtility
        self.state = state
        self.partial = partial
    
    # getUtility returns expected utility
    def getExpectedUtility(self):
        return self.expectedUtility
    
    # getState returns state
    def getState(self):
        return self.state
    
    # getPartial returns partial schedule
    def getPartial(self):
        return self.partial

# The Scheduler class is the research algorithm
class Scheduler:
  
    # __init__ constructs Scheduler object
    def __init__(self, countries):
        self.countries = countries
    
    # search searches for the best schedule
    def search(self, maxDepth, maxSize):
        pq = []
        visited = []
        result = []
        
        startState = self.countries.getStateStatus()
        item = Part(0, startState, [])
        heapq.heappush(pq, item)
        while pq:
            cur = heapq.heappop(pq)
            
            state = cur.getState()
            schedule = cur.getPartial()
            
            if len(schedule) == maxDepth:
               
                heapq.heappush(result, cur)
            
            else:
                if state not in visited:
                    
                    visited.append(state)
                    
                    for successor in self.countries.getSuccessors(state):
                        nextState = successor[0]
                        nextAction = successor[1]
                        nextUtility = self.countries.getExpectedUtility(state, nextState, len(schedule) + 1, nextAction)
                        
                        nextSchedule = schedule + [[nextAction.toString(), nextUtility]]
                        nextItem = Part(-1 * nextUtility, nextState,
                                        copy.deepcopy(nextSchedule))
                        #if nextState not in visited:
                           # heapq.heappush(pq, nextItem)
                            
                            if len(pq) > maxSize:
                                pq.pop()
        return result
