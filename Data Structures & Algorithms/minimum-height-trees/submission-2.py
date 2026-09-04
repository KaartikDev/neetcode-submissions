class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #O(V(V+E)) --> calc bfs for all nodes
        # E = n-1, #O(V^2), --> 400 * 10 ^ 6  as V <= 20k

        if not edges:
            return [0]
        
        adjMap = {}
        for a,b in edges:
            if a not in adjMap:
                adjMap[a] = []
            if b not in adjMap:
                adjMap[b] = []
            adjMap[a].append(b)
            adjMap[b].append(a)

        
        def minHeight(head):
            q = deque([head])
            visited = set([head])
            height = 0
            while q:
                height+=1
                for _ in range(len(q)):
                    curr = q.popleft()
                    for nei in adjMap[curr]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            return height
        
        heights = {}
        minSeen = float('inf')
        for currRoot in range(n):
            heights[currRoot] = minHeight(currRoot)
            minSeen = min(minSeen,heights[currRoot])
        
        # print(heights)
        res = []
        for currRoot in heights:
            if heights[currRoot] == minSeen:
                res.append(currRoot)
        return res

