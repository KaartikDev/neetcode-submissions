class MinStack:

    def __init__(self):
        self.foundMin = float('inf')  
        self.stack = []
        self.mappedMin = {} #each node stores what the found min is when it was pushed
    
    def push(self, val: int) -> None:
        if val not in self.mappedMin: #create a dict entry mapping current value to the found(works for repeats)
            self.mappedMin[val] = [self.foundMin]
        else:
            self.mappedMin[val].append(self.foundMin)
    
        self.foundMin = min(val,self.foundMin) #update the found min(do this after mapping so we can go backward)
        self.stack.append(val) #add to stack
        
    def pop(self) -> None:
        temp = self.stack.pop() #pop value
        self.foundMin = self.mappedMin[temp].pop() #update found min to previously connected        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.foundMin
        
