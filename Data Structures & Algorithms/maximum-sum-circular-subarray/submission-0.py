class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        

        #idea do normal O(n) max subarray start at different n --> n^2 time
        # 30000^2 = 300 000 000, not insane for python

        def maxSubArrFrom(i):
            N = len(nums)
            count = 0
            currSum = 0
            best = -float('inf')
            while count < N:
                validIndex = i % N
                currSum = max(nums[validIndex],currSum+nums[validIndex])
                best = max(currSum,best)
                i+=1
                count+=1
            return best
        

        res = -float('inf')
        for i in range(len(nums)):
            res = max(res,maxSubArrFrom(i))
        return res

