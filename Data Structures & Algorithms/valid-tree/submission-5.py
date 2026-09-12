class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #n-1 edges
        #acyclic
        #fully connected
        
        if len(edges) != n-1:
            return False
        
        if n == 1: #single node graph
            return True

        #now build adj map
        adjMap = {}
        degree = {}
        for u,v in edges:
            if u not in adjMap:
                adjMap[u] = []
            if v not in adjMap:
                adjMap[v] = []
            
            adjMap[u].append(v)
            adjMap[v].append(u)
            degree[u] = degree.get(u,0)+1
            degree[v] = degree.get(v,0)+1

        # print(adjMap,degree)
        #now do kahans on UNDIRECTED graph (delete nodes with degree 1 as they are leaves)
        leaves = deque()
        visited = set()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
                visited.add(i)
            
        
        while leaves:
            curr = leaves.popleft()
            
            
            for nei in adjMap[curr]:
                degree[nei]-=1
                if degree[nei] == 1:
                    leaves.append(nei)
                    visited.add(nei)
        
        return len(visited) == n
        