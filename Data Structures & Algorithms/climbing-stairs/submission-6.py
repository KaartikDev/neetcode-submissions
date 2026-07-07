class Solution:
    def climbStairs(self, n: int) -> int:

        # climb(n) = climb(n-1) + climb(n-1)
        memo = {}

        def climb(x):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x == 2:
                return 2
            if x in memo:
                return memo[x]
            
            memo[x] = climb(x-1) + climb(x-2)
            return memo[x]



        return climb(n)