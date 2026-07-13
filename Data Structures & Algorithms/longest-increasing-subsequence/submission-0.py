class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} #bestLen, minNum
        best = 0 
        def dfs(i, prev_index):
            if i == len(nums):
                return 0
            if (i,prev_index) in memo:
                return memo[(i,prev_index)]
            
            #skip
            skip = dfs(i+1,prev_index)
            
            #take
            take = 0
            if prev_index == -1 or nums[i] > nums[prev_index]:
                take = 1+dfs(i+1,i)
            memo[(i,prev_index)] = max(skip,take)
            return memo[(i,prev_index)]      

        return dfs(0,-1)