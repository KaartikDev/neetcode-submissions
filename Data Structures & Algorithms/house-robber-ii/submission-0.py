class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #still dfs(i) = max(cost[i]+dfs(i-2),dfs(i-1))
        
        if len(nums) == 1:
            return nums[0]

        def dfs(l,r):
            memo = {}

            def helper(i):
                if i > r:
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(nums[i]+helper(i+2), helper(i+1))
                return memo[i]
            
            return helper(l)

        return max(dfs(0,len(nums)-2), dfs(1,len(nums)-1))

        #top down dp 
