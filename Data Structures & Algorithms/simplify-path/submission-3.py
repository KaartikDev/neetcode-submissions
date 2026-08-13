class Solution:
    def simplifyPath(self, path: str) -> str:

        originalStack = path.split("/")
        # print(originalStack)

        cleanedStack = []

        for el in originalStack:
            if el == "" or el == ".": #empty change or curr directory --> skip
                continue
            elif el == "..": # pop off prev cuz we in parent now
                if cleanedStack: 
                    cleanedStack.pop()
            else:
                cleanedStack.append(el)
        # print(cleanedStack)

        res = "/".join(cleanedStack)
        return "/"+res
