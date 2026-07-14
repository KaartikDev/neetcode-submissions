class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        #if sum not even we cant partion into 2 whole subset halfsums

        halfSum = sum(nums)//2

        memo = {}

        def dfs(i,halfSum):
            if halfSum == 0:
                return True
            if i == len(nums):
                return False
            if (i,halfSum) in memo:
                return memo[(i,halfSum)]
            #skip
            skip = dfs(i+1, halfSum)

            #take
            take = dfs(i+1,halfSum-nums[i])

            memo[(i,halfSum)] = skip or take
            return memo[(i,halfSum)]
        
        return dfs(0,halfSum)