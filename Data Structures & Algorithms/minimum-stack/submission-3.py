class MinStack:

    def __init__(self):
        # minSeen = float('inf')
        self.minStack = []
        self.normStack = []

    def push(self, val: int) -> None:
        self.normStack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])


    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()
        if self.normStack:
            self.normStack.pop()


    def top(self) -> int:
        return self.normStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
