class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = set(["+","*","-","/"])

        stack = []
        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            elif c == "+":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1+op2)
            elif c == "*":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1*op2)
            elif c == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1-op2)
            elif c == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1/op2))
        
        return stack[-1]

    
    def evalExpression(tokens):
        pass