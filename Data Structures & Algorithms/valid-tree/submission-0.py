class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #n-1 edges
        #acyclic
        #fully connected
        if len(edges) != n-1:
            return False
        
        #now to check for cycles
        #build adj list and then keep track of parent bfs
        def buildAdjList(V_count,E):
            adjList = []
            for i in range(V_count):
                adjList.append([])
            
            for edge in E:
                u = edge[0]
                v = edge[1]
                adjList[u].append(v)
                adjList[v].append(u)
            
            return adjList
        
        adjList = buildAdjList(n,edges)

        #do parent bfs
        queue = deque([(0,-1)])
        visited = set([0])
        while queue:
            curr, parent = queue.popleft()

            for neighbor in adjList[curr]:
                if neighbor in visited and neighbor != parent:
                    return False
                elif neighbor not in visited:
                    queue.append((neighbor,curr))
                    visited.add(neighbor)
        
        if len(visited) == n:
            return True
        else:
            return False



