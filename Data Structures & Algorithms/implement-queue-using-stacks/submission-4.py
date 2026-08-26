class MyQueue:

    def __init__(self):
        self.st = []

        # 1 2 3 --> 3 (queue)
        # 3 2 1 --> 1 (stack)

    def push(self, x: int) -> None:
        
        #rotate into stack form
        temp = []
        while self.st:
            temp.append(self.st.pop())
        self.st = temp


        # add new element
        self.st.append(x)

        #rotate back into queue form
        temp = []
        while self.st:
            temp.append(self.st.pop())
        self.st = temp
        
        print(self.st)

    def pop(self) -> int:

        
        return self.st.pop()
        

    def peek(self) -> int:

        return self.st[-1]

        

    def empty(self) -> bool:
        return len(self.st) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()