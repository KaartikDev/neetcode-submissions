class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        best = -float("inf")
        currSum = 0

        for i in range(len(nums)):
            currSum+=nums[i]
            if nums[i] > currSum:
                currSum = nums[i]
            
            best = max(currSum, best)
        return best

