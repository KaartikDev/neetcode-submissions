class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #what are the states?
        #target, numIndex?

        memo = {}

        def dp(amtLeft, numIndex):
            if amtLeft == 0 and numIndex == len(nums):
                return 1
            if numIndex >= len(nums):
                return 0
            if (amtLeft,numIndex) in memo:
                return memo[(amtLeft,numIndex)]
            
            add = dp(amtLeft-nums[numIndex],numIndex+1)
            subtract = dp(amtLeft+nums[numIndex],numIndex+1)

            memo[(amtLeft,numIndex)] = add + subtract
            return memo[(amtLeft,numIndex)]
        
        return dp(target,0)