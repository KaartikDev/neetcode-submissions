class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        
        

        buckets = []
        for i in range(len(nums)):
            buckets.append([])
        # print(buckets)
        # print(freqMap)
        for key in freqMap:
            # print(freqMap[key])
            buckets[freqMap[key]-1].append(key)
        
        ans = []
        for i in range(len(nums)-1,-1,-1):
            # print(ans)
            if len(ans) == k:
                return ans
            else:
                while buckets[i]:
                    temp = buckets[i].pop()
                    ans.append(temp)
        return ans
            
