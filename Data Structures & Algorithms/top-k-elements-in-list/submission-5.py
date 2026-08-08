class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = {}
        highestFreq = 0
        for n in nums:
            freqMap[n] = freqMap.get(n,0)+1
            highestFreq = max(freqMap[n],highestFreq)
        
        buckets = [[] for _ in range(highestFreq+1)]

        for key in freqMap:
            freq = freqMap[key]
            buckets[freq].append(key)
        
        res = []

        for i in range(len(buckets)-1,-1,-1):
            while buckets[i] and len(res) < k:
                res.append(buckets[i].pop())
        return res

        print(buckets)


        











        # freqMap = {}

        # for num in nums:
        #     if num not in freqMap:
        #         freqMap[num] = 1
        #     else:
        #         freqMap[num] += 1
        
        

        # buckets = []
        # for i in range(len(nums)):
        #     buckets.append([])
        # # print(buckets)
        # # print(freqMap)
        # for key in freqMap:
        #     # print(freqMap[key])
        #     buckets[freqMap[key]-1].append(key)
        
        # ans = []
        # for i in range(len(nums)-1,-1,-1):
        #     while buckets[i]:
        #         ans.append(buckets[i].pop())
        #         if len(ans) == k:
        #             return ans

        # return ans
            
