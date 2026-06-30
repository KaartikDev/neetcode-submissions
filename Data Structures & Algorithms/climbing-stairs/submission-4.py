class Solution:
    def climbStairs(self, n: int) -> int:

        #climbStair(n) = climbStair(n-1) + climbStair(n-2)
        
        memo = {}

        def dfs(x):
            if x in memo:
                return memo[x]
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x == 2:
                return 2
            
            memo[x] = dfs(x-1) + dfs(x-2)
            return memo[x]
        return dfs(n)

        