class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #hmmm labeled 1 to n
        # want LAST edge in egdes
        #idea --> make list edges in current cyle see whcih element comes last
        # would need to check posiotn of each edge --> O(1) time O(E) space w/ hash map

        #how do u list edges in current cycle, wiuld want to do dfs for this


        #step 1: reindex to zero
        for edge in edges:
            edge[0]-=1
            edge[1]-=1
        #step 2 buld adjlist
        def buildAdjList(V_count,E):
            adjList=[]
            for i in range(V_count):
                adjList.append([])
            
            for edge in E:
                a = edge[0]
                b = edge[1]
                adjList[a].append(b)
                adjList[b].append(a)
            return adjList
        #len(edges) == n as orignally n-1 edges
        n = len(edges)
        adjList = buildAdjList(n,edges)

        #use dfs to find cycle
        parent = [-1] * n
        visited = [False] * n
        in_path = set()
        cycle_edges = set()

        def dfs(node):
            visited[node] = True
            in_path.add(node)

            #do dfs
            for neighbor in adjList[node]:
                if neighbor == parent[node]:
                    continue
                if not visited[neighbor]:
                    parent[neighbor] = node
                    if dfs(neighbor): #we found a cycle alr created edges can stop now
                        return True
                
                elif neighbor in in_path:
                    #now build the cycle
                    curr = node
                    while curr != neighbor:
                        cycle_edges.add(tuple(sorted((curr, parent[curr]))))
                        curr = parent[curr]
                    cycle_edges.add(tuple(sorted((node, neighbor))))
                    return True
            
            in_path.remove(node)
            return False
        dfs(0)
        # print(cycle_edges)
        
        edgeMap = {}
        for i in range(n):
            edge = edges[i]
            hashEdge = tuple(edge)
            edgeMap[hashEdge] = i

        maxIndex = -1
        for edge in cycle_edges:
            maxIndex = max(maxIndex,edgeMap[edge])
        # print(maxIndex)
        #reindex to 1
        for edge in edges:
            edge[0]+=1
            edge[1]+=1
        
        return edges[maxIndex]

