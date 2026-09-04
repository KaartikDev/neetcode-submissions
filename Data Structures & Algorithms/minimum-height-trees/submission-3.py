class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # #O(V(V+E)) --> calc bfs for all nodes
        # # E = n-1, #O(V^2), --> 400 * 10 ^ 6  as V <= 20k

        if not edges:
            return [0]
        if n <= 2:
            return list(range(n))
        
        adjMap = {}
        degree = {}
        for a,b in edges:
            if a not in adjMap:
                adjMap[a] = []
                
            if b not in adjMap:
                adjMap[b] = []
            
            adjMap[a].append(b)
            adjMap[b].append(a)

            degree[a] = degree.get(a,0)+1
            degree[b] = degree.get(b,0)+1
        
        #now run kahans algo on UNDIRECTED graph
        leaves = deque()
        visited = set()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
                visited.add(i)
        
        deleted = 0
        while leaves and n-len(visited)>2: #want to stop when we get to final 2 layers
            for _ in range(len(leaves)):
                curr = leaves.popleft()                
                for nei in adjMap[curr]:
                    degree[nei]-=1
                    if nei not in visited and degree[nei] == 1:
                        visited.add(nei)
                        leaves.append(nei)
        
        # print(visited)
        allNodes = set(range(n))
        return list(allNodes-visited)
        # print(n)
        # def minHeight(head):
        #     q = deque([head])
        #     visited = set([head])
        #     height = 0
        #     while q:
        #         height+=1
        #         for _ in range(len(q)):
        #             curr = q.popleft()
        #             for nei in adjMap[curr]:
        #                 if nei not in visited:
        #                     visited.add(nei)
        #                     q.append(nei)
        #     return height
        
        # heights = {}
        # minSeen = float('inf')
        # for currRoot in range(n):
        #     heights[currRoot] = minHeight(currRoot)
        #     minSeen = min(minSeen,heights[currRoot])
        
        # # print(heights)
        # res = []
        # for currRoot in heights:
        #     if heights[currRoot] == minSeen:
        #         res.append(currRoot)
        # return res

