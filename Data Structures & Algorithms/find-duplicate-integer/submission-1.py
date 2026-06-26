class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        
        

        FreqMap = {}
        for num in nums:
            if num in FreqMap:
                return num
            else:
                FreqMap[num]=0
        return -1
        