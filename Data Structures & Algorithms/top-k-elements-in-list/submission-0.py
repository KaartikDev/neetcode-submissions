class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxCount = 0

        freqMap = {}
        
        
        for num in nums: #O(N) time O(N) space
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
            
        
        #using bucket sort with the freqencies as the buckets
        bucketMap = {}

        for i in range(len(nums)): #O(N) time O(N) space
            bucketMap[i+1] = [] #initialize empty list bucketMap, include all possible frequencies as keys(1 to n)
        
        for val in freqMap: #fill in bucket map with our values
            currFrq = freqMap[val]
            bucketMap[currFrq].append(val)
        
        j = len(nums) #start from highest possible frequency and move down
        ansList = []

        while j > 0 and len(ansList) < k:
            if bucketMap[j]:
                while bucketMap[j] and len(ansList) < k: #clear out al the elements at this bucket, stop when answer list is fill
                    ansList.append(bucketMap[j][-1]) #append the last element of in current bucket that appered with frequency j
                    bucketMap[j].pop()
            j-=1
        
        return ansList



        