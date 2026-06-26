class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # lets see cases
        # for n == 1: ()
        # for n == 2: ()(), (())
        # for n == 3: ()()(), (())(), ()(()), ((())), (()())
        # at each point w can either start a new "(" and hold off on ")"
        # or we can add full "()"
        res = []
        curr = []


        def dfs(openCount,closeCount):
            if len(curr) == 2*n and openCount == closeCount:
                res.append("".join(curr))
                return None
            if len(curr) > 2*n:
                return None
            if closeCount > openCount:
                return None
            
            if openCount < n:
                curr.append("(")
                openCount+=1
                dfs(openCount, closeCount)
                curr.pop()
                openCount-=1
            
            if closeCount < n:
                curr.append(")")
                closeCount+=1
                dfs(openCount, closeCount)
                curr.pop()
                closeCount-=1
            
        
        dfs(0,0)
        return res
            
            


        










