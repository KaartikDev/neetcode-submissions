class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        maxLenFound = 1
        l = 0
        r = len(nums) - 1

        fullSet = set(nums)
        checkedSet = set()
        i = 0
        while i < len(nums):
            currLen = 0

            if nums[i]-1 not in fullSet and nums[i] not in checkedSet: #only start a search if a numbers
                checkedSet.add(nums[i])
                temp = nums[i]+1
                currLen+=1
                while temp in fullSet:
                    currLen+=1
                    checkedSet.add(temp)
                    temp+=1
            maxLenFound = max(maxLenFound,currLen)
            i+=1
        return maxLenFound
                



