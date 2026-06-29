class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we could build adj list 
        # each slot will consist of neighbor dictionary mapping node to time
        # this graph is directed!!
        # then run dijkstra for all nodes connected to k

        if n == 0: #empty graph gaurd
            return 0


        def buildAdjList(vert_count, weighted_edges):
            #need to do n+1 as indexing 1 to n:
            adjList = [{} for i in range(vert_count+1) ]
            for edge in weighted_edges:
                u = edge[0]
                v = edge[1]
                cost = edge[2]

                u_neighbors = adjList[u]
                if v not in u_neighbors:
                    u_neighbors[v] = cost
                elif cost < u_neighbors[v]:
                    u_neighbors[v] = cost
            
            # for i in range(1,len(adjList)):
            #     print(i,adjList[i])
            return adjList
        
        adjList = buildAdjList(n, times)


        def dijsktra(adjList, k):

            distances = [float('inf') for i in range(len(adjList))]
            distances[k] = 0

            pq = [(0,k)]
            heapq.heapify(pq)
            while pq:
                currDist, currNode = heapq.heappop(pq)
                if currDist > distances[currNode]:
                    continue
                
                for neighbor in adjList[currNode]:
                    v = neighbor
                    cost = adjList[currNode][neighbor]
                    distanceToV = currDist + cost
                    
                    if distanceToV < distances[v]:
                        distances[v] = distanceToV
                        heapq.heappush(pq, (distanceToV, v))
            
            return distances
        distancesToNodes = dijsktra(adjList, k)
        distancesToNodes = distancesToNodes[1:] #get rid of node 0 as it never existed (due to index by 1)
        longestTime = max(distancesToNodes)
        if longestTime == float('inf'):
            return -1
        else:
            return longestTime


        