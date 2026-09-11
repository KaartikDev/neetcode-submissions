class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we could build adj list 
        # each slot will consist of neighbor dictionary mapping node to time
        # this graph is directed!!
        # then run dijkstra for all nodes connected to k


        if n == 0:
            return 0
        

        adjMap = {}
        for u,v,cost in times:
            if u not in adjMap:
                adjMap[u] = {}
            adjMap[u][v] = cost
        

        #run dijsktras
        times = [float('inf')] * (n+1)
        # print(adjMap,times)
        times[k] = 0
        pq = [(0,k)] #currTime, currNode

        while pq:
            currTime, currNode = heapq.heappop(pq)
            if currTime > times[currNode]:
                continue
            
            for nei in adjMap.get(currNode,[]):
                delay = adjMap[currNode][nei]
                if currTime+delay < times[nei]:
                    times[nei] = currTime+delay
                    heapq.heappush(pq,(currTime+delay,nei))
        print(times)
        times = times[1:]#cut off node 0 as 1 indexed nodes
        return max(times) if max(times) < float('inf') else -1






