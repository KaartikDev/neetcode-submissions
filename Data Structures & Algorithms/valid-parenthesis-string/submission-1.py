class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        astStack = []

        
        for i in range(len(s)):
            if s[i] == "*": #save for later
                astStack.append(i)
            elif s[i] == "(":
                openStack.append(i)
            elif s[i] == ")":
                if openStack: #take from open if possible
                    openStack.pop()
                elif astStack: #take from ast if needed
                    astStack.pop()
                else:
                    return False

        while openStack and astStack:
            if openStack[-1] < astStack[-1]: #open appeared frist
                openStack.pop()
                astStack.pop()
            else:
                break

        return len(openStack) == 0