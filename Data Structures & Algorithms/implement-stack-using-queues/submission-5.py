class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

        #roate it n-1 times
        n = len(self.q1)
        for i in range(n-1):
            temp = self.q1.popleft()
            self.q1.append(temp)



    def pop(self) -> int:
        assert len(self.q1) >= 1, 'empty stack got popped'
        
        return self.q1.popleft()
        

    def top(self) -> int:
        assert len(self.q1) >= 1, 'empty stack got topped'
        
    
        return self.q1[0]
    

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()