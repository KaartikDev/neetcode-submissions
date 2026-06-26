class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1

        bucketArr = []
        for i in range(len(nums)+1):
            bucketArr.append([])
        
        # print(freqMap)
        # print(bucketArr[0])
        for key in freqMap:
            
            bucketArr[freqMap[key]].append(key)
            # print(freqMap[key], key, bucketArr)
        
        # print(bucketArr)
        ans = []
        p = len(bucketArr) - 1
        while p >= 0 and len(ans) != k:
            while bucketArr[p]:
                temp = bucketArr[p].pop()
                ans.append(temp)
            p-=1
        print(ans)
        return ans
        #Total time complexity O(N)
        #Total  space compelxity O(N)



        