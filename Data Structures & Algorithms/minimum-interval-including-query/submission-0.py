class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        #idea: match each querry to its solution
        qMap = {}
        for i in range(len(queries)):
            qMap[queries[i]] = -1
        
        #now we can sort copy of querries and later rebuild w/ correct order
        sortedQuerries =  deque(sorted(set(queries)))
        #use queue so we can pop form left, and set so only process querry point once
        # print(sortedQuerries)
        
        #we sort intervals by start time
        heapByStart = intervals.copy()
        heapq.heapify(heapByStart)
       

        heapBySize = []

        while sortedQuerries:
            currQ = sortedQuerries.popleft()
            
            # add all itnervals that start before currQ
            #querries are stirctly increasing so this is safe
            while heapByStart and heapByStart[0][0] <= currQ:
                
                startTime, endTime = heapq.heappop(heapByStart)
                size = endTime - startTime + 1

                heapq.heappush(heapBySize,(size,endTime))
            
            #remove all intervals that end before currQ
            #querries are stirctly increasing so this is safe
            while heapBySize and heapBySize[0][1] < currQ:
                heapq.heappop(heapBySize)
            
            #return top of heap if it exists, default in map is -1
            if heapBySize:
                qMap[currQ] = heapBySize[0][0]
        
        # print(qMap)
        
        #rebuild in order

        res = []
        for j in range(len(queries)):
            res.append(qMap[queries[j]])
        return res


                      
            



    



