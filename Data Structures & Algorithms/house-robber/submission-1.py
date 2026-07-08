class Solution:
    def rob(self, nums: List[int]) -> int:
        # u can reither rob ith house or i+2 house.
        
        memo = {}

        def dfs(i):
            if i < 0 or i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            
            
       
            memo[i] = max(dfs(i-2)+nums[i], dfs(i-1))
            return memo[i]
        
        
        return dfs(len(nums)-1)