class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        
        halfSum = sum(nums)/2
        memo = {}
        def dfs(i,target):
            if target == 0:
                return True
            if target < 0 or i == len(nums):
                return False
            if (i,target) in memo:
                return memo[(i,target)]
            
            memo[(i,target)] = dfs(i+1,target) or dfs(i+1,target-nums[i])
            return memo[(i,target)]
        
        return dfs(0,halfSum)
            