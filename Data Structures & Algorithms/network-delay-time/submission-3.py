class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we could build adj list 
        # each slot will consist of neighbor dictionary mapping node to time
        # this graph is directed!!
        # then run dijkstra for all nodes connected to k

        if n == 0:
            return 0
        

        adjMap = {}
        for u,v,t in times:
            if u not in adjMap:
                adjMap[u] = {}
            if v not in adjMap:
                adjMap[v] = {}
            
            adjMap[u][v]=t
        

        #now to do dijkstras
        #O(V+E)?
        dist = [float("inf")]*(n+1)

        pq = [(0,k)]
        dist[k] = 0

        while pq:
            currDist,currNode, = heapq.heappop(pq)
            if currDist > dist[currNode]:
                continue
            
            for nei in adjMap[currNode]:
                nextCost = adjMap[currNode][nei]
                if currDist+nextCost < dist[nei]:
                    dist[nei] = currDist+nextCost
                    heapq.heappush(pq,(currDist+nextCost,nei))
        print(dist)
        return max(dist[1:]) if max(dist[1:]) < float('inf') else -1

