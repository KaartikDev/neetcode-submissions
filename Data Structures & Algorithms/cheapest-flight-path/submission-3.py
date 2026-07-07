class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float('inf') for i in range(n)]
        prices[src] = 0
            
        for _ in range(k+1):
            tmpPrices = prices.copy()
            for u,v,w in flights:
                if prices[u] == float("inf"):
                    continue
                if prices[u] + w < tmpPrices[v]:
                    tmpPrices[v] = prices[u]+w
            prices = tmpPrices

        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]

        # define prices to be array len n holding inf for each
        # set src price to zero and iter for k+1 time
        # on each iter of for loop, prices reflects best path if allowed #iter stops.
        # price will have inf distance if it has been unreachable
        # we check at most one more flight(edge) from each of the non inf prices
        # if after k+1 flights, dest still inf price, it is unreachable
        # O(k*len(flights))

        
        



        #below is wrong!!
        #build full adj map
        # then do bfs for airports within k+1 stops (k+1 levels away)
        # then run dijkstras
        
        # def buildAdjMap(edges):

        #     adjMap = {}
        #     for e in edges:
        #         u = e[0]
        #         v = e[1]

        #         cost = e[2]
        #         if u not in adjMap:
        #             adjMap[u] = {v:cost}
        #         else:
        #             adjMap[u][v] = cost
            
        #     return adjMap
        
        # adjMap = buildAdjMap(flights)
        # print(adjMap)




        # def bellmanFord(adjMap, src, k, n):                    

            
        # dist = dijkstra(reachableAirports, src, k, n)
        # print(dist)
        # if dist[dst] == float('inf'):
        #     return -1
        # else:
        #     return dist[dst]



        # #doenst work as trimming doesnt help can still tkae wierd path
        #         #need to do bfs from src for k+1 levels
        # # def bfs(adjMap, k, src):
        # #     level = 0
        # #     queue = deque([src])
        # #     seen = set([src])
            
        # #     reachableAirports = {src:adjMap.get(src, {})}
            
        # #     while queue and level<k+1:
        # #         for _ in range(len(queue)):
        # #             curr = queue.popleft()
        # #             for nei in adjMap.get(curr, {}):
        # #                 if nei not in seen:
        # #                     seen.add(nei)
        # #                     reachableAirports[nei] = adjMap.get(nei, {})
        # #                     queue.append(nei)

        # #         level+=1
        # #     return reachableAirports

        # # reachableAirports = bfs(adjMap, k, src)
        # # print(reachableAirports)
