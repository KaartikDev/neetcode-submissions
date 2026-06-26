class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])

        
        numFreqMap = {}

        for num in nums:
            if num not in numFreqMap:
                numFreqMap[num] = 1
            else:
                numFreqMap[num] += 1
        
        for key in numFreqMap:
            buckets[numFreqMap[key]].append(key)
        
        j = len(nums) 
        ans = []

        while j >= 0 and len(ans) != k:
            while buckets[j] and len(ans) != k:
                ans.append(buckets[j][-1])
                buckets[j].pop()
            j-=1
        
        return ans




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
            
