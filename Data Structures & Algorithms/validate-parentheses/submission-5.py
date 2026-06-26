class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        openSet = set(['(','[','{'])
        for c in s:
            if c in openSet:
                stack.append(c)
            else:
                # print(c)
                if not stack: 
                    return False
                
                if stack[-1] != "(" and c == ')':
                    return False
                elif stack[-1] != "{" and c == '}':
                    return False
                elif stack[-1] != "[" and c == ']':
                    return False
                stack.pop()
        
        return len(stack) == 0