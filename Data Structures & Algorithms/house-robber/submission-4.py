class Solution:
    def rob(self, nums: List[int]) -> int:
        # u can reither rob ith house or i+2 house.
        
        # dfs(i) = max(nums[i] + dfs(i-2), dfs(i-1))

        memo = {}

        def dfs(i):
            # print("entry i=",i)
            if i < 0:
                return 0
            if i == 0:
                return nums[i]
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i]+dfs(i-2), dfs(i-1))

            return memo[i]
        
        return dfs(len(nums)-1)