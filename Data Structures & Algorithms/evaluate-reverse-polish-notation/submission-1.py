class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack= [] #valid stack garunteed
        operators = set(['+','-','/','*'])
        for tok in tokens:
            if tok in operators:
                num2 = int(tokenStack.pop())
                num1 = int(tokenStack.pop())
                if tok == '*':
                    tokenStack.append(num1 * num2)
                elif tok == "/":
                    tokenStack.append(num1 / num2)
                elif tok == "+":
                    tokenStack.append(num1+num2)
                else:
                    tokenStack.append(num1-num2)
            else:
                tokenStack.append(tok)
        
        return int(tokenStack[0])
                

        