class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = []
        
        openP = set(['(','{','['])
        

        for c in s:
            print(parenStack)
            if c in openP:
                parenStack.append(c)
            else:
                if len(parenStack) == 0: #no matching open exists
                    return False

                if c == ')' and parenStack.pop() != '(': #wrong types of matching
                    return False
                if c == '}' and parenStack.pop() != '{':
                    return False
                if c == ']' and parenStack.pop() != '[':
                    return False
        
        return len(parenStack) == 0

