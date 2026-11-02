class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} 
        best = 0 
        def dfs(i, prevBound):
            if i == len(nums):
                return 0
            if (i,prevBound) in memo:
                return memo[(i,prevBound)]
            
            #skip
            skip = dfs(i+1,prevBound)
            
            #take
            take = 0
            if nums[i] > prevBound:
                take = 1+dfs(i+1,nums[i])
            memo[(i,prevBound)] = max(skip,take)
            return memo[(i,prevBound)]      

        return dfs(0,-float('inf'))