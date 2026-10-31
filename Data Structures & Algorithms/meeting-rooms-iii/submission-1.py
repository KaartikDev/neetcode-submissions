class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #heap end time, roomnumber

        useCount = {}
        availablePQ = []
        for i in range(n):
            useCount[i] = 0
            availablePQ.append(i)
        
        inUsePQ = []
        meetings.sort()
        
        for start,end in meetings:

            while inUsePQ and start >= inUsePQ[0][0]:
                oldTime, roomNumber = heapq.heappop(inUsePQ)
                heapq.heappush(availablePQ, roomNumber)
            
            if availablePQ:
                roomNumber = heapq.heappop(availablePQ)
                heapq.heappush(inUsePQ, (end,roomNumber))
                useCount[roomNumber]+=1
            else: #if nothng is available eveything is in use
                delayedStart, roomNumber = heapq.heappop(inUsePQ)
                meetingLen = end - start
                heapq.heappush(inUsePQ, (delayedStart+meetingLen,roomNumber))
                useCount[roomNumber]+=1

            
        
        print(useCount)
        maxUses = 0
        res = -1
        for i in range(n):
            if useCount[i] > maxUses:
                maxUses = useCount[i]
                res = i
        return res



