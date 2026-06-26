class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: #Empty list gaurd
            return 0

        setNums = set(nums)

        maxSeq = 1
        for num in nums:
            currSeq = 1
            if num-1 not in setNums:
                nextNum = num+1
            
                for i in range(len(nums)):
                    if nextNum in setNums:
                        nextNum += 1
                        currSeq += 1
            
            maxSeq = max(maxSeq,currSeq)
        return maxSeq
        