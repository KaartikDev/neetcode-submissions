class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # make adj map
        # need lexiicographically shortest path that covers all edges and is connected


        def buildAdjMap(edges):
            adjMap = {}
            for edge in edges:
                src = edge[0]
                dest = edge[1]
                if src not in adjMap:
                    adjMap[src] = [dest]
                else:
                    heapq.heappush(adjMap[src],dest)
            return adjMap
        
        adjMap = buildAdjMap(tickets)
        # print(adjMap)

        # do a dfs exporlartion till all nodes visted?
        visited = [] # do hierhorz algo (post order dfs)
        def dfs(src):
            while src in adjMap and adjMap[src]:
                dest = heapq.heappop(adjMap[src])
                dfs(dest)
            visited.append(src)
        dfs("JFK")
        visited.reverse()
        return visited

        # O(ElogE) time, O(E) space