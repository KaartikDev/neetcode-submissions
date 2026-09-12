class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []

        for c in s:
            if c == "(" or c=="{" or c=="[":
                stack.append(c)
            else:
                if c == ")" and stack and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False