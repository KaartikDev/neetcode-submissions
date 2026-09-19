class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for c in operations:
            if c == "+": #contraints garuntee existence
                stack.append(stack[-1]+stack[-2])
            elif c == "D":
                stack.append(stack[-1]*2)
            elif c == "C":
                stack.pop()
            else:
                stack.append(int(c))
        return sum(stack)
