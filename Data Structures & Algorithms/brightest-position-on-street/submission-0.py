class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # smallestPos = float('inf')
        # largestPos = -float("inf")
        if not lights: #should never happen by constraints
            return -1
        
        intervals = []

        startEdges = []
        for light in lights:
            start = light[0] - light[1]
            end = light[0] + light[1]
            intervals.append([start,end])
            startEdges.append(start)
            # smallestPos = min(start,smallestPos)
            # largestPos = max(end,largestPos)
        
        # print(intervals)
        
        heapq.heapify(intervals) #sort intervals
        startEdges.sort() #sort start edges
        
        res = [0, -float("inf")] #over lap count, position
        activeHeap = []
 
        for currPos in startEdges:
            while intervals and intervals[0][0] <= currPos:
                heapq.heappush(activeHeap, intervals[0][1])
                heapq.heappop(intervals)
            while activeHeap and activeHeap[0] < currPos:
                heapq.heappop(activeHeap)
            
            if len(activeHeap) > res[0]:
                res = [len(activeHeap),currPos]
        
        return res[1]



        