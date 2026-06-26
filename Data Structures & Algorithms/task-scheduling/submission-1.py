class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        
        #want cpu cycles
        #identical tasks must have n cycles bewtween them


        freqMap = {}

        for t in tasks:
            if t not in freqMap:
                freqMap[t] = 1
            else:
                freqMap[t] += 1
        
        orderQueue = deque()
        taskFreqHeap = []
        heapq.heapify(taskFreqHeap)
        for key in freqMap:
            temp = [freqMap[key]*-1,key]
            heapq.heappush(taskFreqHeap,temp)
        print(taskFreqHeap)

        netCycles = 0
        while taskFreqHeap or orderQueue:

            while orderQueue and (netCycles >= orderQueue[0][1]+n+1):
                reInsert = orderQueue.popleft()[0]
                
                heapq.heappush(taskFreqHeap,reInsert)
            
            if not taskFreqHeap:
                netCycles+=1
                continue
            
            curr = heapq.heappop(taskFreqHeap)
            print(curr,orderQueue)
            curr[0]*=-1
            curr[0]-=1
            curr[0]*=-1
            if curr[0] < 0:
                orderQueue.append([curr,netCycles])
            
            
            netCycles+=1


        return netCycles





