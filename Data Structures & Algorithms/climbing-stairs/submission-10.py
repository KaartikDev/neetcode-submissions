class Solution:
    def climbStairs(self, n: int) -> int:

       #stair(n) = stair(n-1) + stair(n-2)
        memo = {}
        def stair(x):
            if x <= 0:
                return 0
            if x == 1:
                return 1
            if x == 2:
                return 2
            if x in memo:
                return memo[x]
            
            memo[x] = stair(x-1) + stair(x-2)
            return memo[x]
        
        return stair(n)


