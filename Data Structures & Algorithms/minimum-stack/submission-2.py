class MinStack:

    def __init__(self):
        self.foundMin = float('inf')  
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.minStack.append(self.foundMin) #maintain previosly seen min by adding it
        self.foundMin = min(self.foundMin, val) #update to see if current is smallest val
        self.stack.append(val) #add it
        
    
    def pop(self) -> None:
        self.stack.pop() #kill top val
        self.foundMin  = self.minStack.pop() #update curr min to previous seen
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.foundMin
        

    #works but is needlesly complicated
    # def __init__(self):
    #     self.foundMin = float('inf')  
    #     self.stack = []
    #     self.mappedMin = {} #each node stores what the found min is when it was pushed
    
    # def push(self, val: int) -> None:

    #     if val not in self.mappedMin: #create a dict entry mapping current value to the found(works for duplicate values)
    #         self.mappedMin[val] = [self.foundMin]
    #     else:
    #         self.mappedMin[val].append(self.foundMin)
    
    #     self.foundMin = min(val,self.foundMin) #update the found min(do this after mapping so we can go backward)
    #     self.stack.append(val) #add to stack
        
    # def pop(self) -> None:
    #     temp = self.stack.pop() #pop value
    #     self.foundMin = self.mappedMin[temp].pop() #update found min to previously connected    

    #     if self.mappedMin[temp] == []: #delete map entry if there are no more existing min values (value does nto excist in stack)
    #         del self.mappedMin[temp]

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.foundMin
        
