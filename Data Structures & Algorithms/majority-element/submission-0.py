class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = {}

        for n in nums:
            freqMap[n] = freqMap.get(n,0) + 1
        

        bestFreq = 0
        res = None

        for key in freqMap:
            if freqMap[key] > bestFreq:
                bestFreq = freqMap[key]
                res = key
        
        return res
