class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def buildAdjList(V_count,E):
            adjList = []
            for i in range(V_count):
                adjList.append([])
            
            for edge in E:
                a = edge[0]
                b = edge[1]
                adjList[a].append(b)
                adjList[b].append(a)
            return adjList

        adjList = buildAdjList(n,edges)

        visited = set()
        def bfs(i): #true if ran else false
            if i in visited:
                return False
            queue = deque([i])
            
            while queue:
                curr = queue.popleft()
                for neighbor in adjList[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return True
        
        regions = 0
        for i in range(n):
            if bfs(i):
                regions+=1
        
        return regions

