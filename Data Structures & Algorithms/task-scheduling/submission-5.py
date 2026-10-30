class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)

        freqMap = {} #O(m) build freqMap
        for t in tasks:
            freqMap[t] = freqMap.get(t,0)+1
        
        # always do AVAILABLE task with most remaining
        # use heap to get most remaining
        # how do we track availability? --> another heap by times

        available = []
        for t in freqMap:
            heapq.heappush_max(available,(freqMap[t],t))
        
        cooldown = []

        currTime = 0
        while available or cooldown:
            # add in any possible available
            while cooldown and currTime >= cooldown[0][0]:
                availTime, availTask = heapq.heappop(cooldown)
                heapq.heappush_max(available,(freqMap[availTask],availTask))
            
            #proc
            frq, procT = heapq.heappop_max(available)
            freqMap[procT]-=1
            currTime+=1
 
            #put on coolDown
            if freqMap[procT] > 0:
                heapq.heappush(cooldown, (currTime+n,procT))
            
            #jump time forward if all on cooldown
            if not available and cooldown:
                currTime = cooldown[0][0]
        return currTime

            




        

        