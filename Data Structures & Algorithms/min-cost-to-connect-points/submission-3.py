class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #need to build MST 
        #use kruskals
        
        #calculate all possible edges and then sort them to be in increasing weight
        #use heap
        edgeHeap = []
        edgeSet = set()
        
        #use tuple so points can be hashed
        tupledPoints = [tuple(p) for p in points]

        for src in tupledPoints:
            for dest in tupledPoints: 
                if src == dest or (dest,src) in edgeSet: #skip self/duplicate edges
                    continue
                    
                manDist = abs(src[0]-dest[0]) + abs(src[1]-dest[1])
                heapq.heappush(edgeHeap,(manDist,src,dest))
                edgeSet.add((src,dest))
        # print(edgeHeap)

        #DSU to prevent cycles
        parent = list(range(len(points)))
        rank = [0] * len(points)

        def findParent(x):
            if parent[x] != x:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(x,y):
            xRankIndex = findParent(x)
            yRankIndex = findParent(y)
            if xRankIndex == yRankIndex:
                return False
            
            if rank[xRankIndex] < rank[yRankIndex]:
                parent[xRankIndex] = yRankIndex
            elif rank[xRankIndex] > rank[yRankIndex]:
                parent[yRankIndex] = xRankIndex
            else:
                parent[yRankIndex] = xRankIndex
                rank[xRankIndex]+=1
            return True
        
        res = 0
        edges_used = 0
        pointToIndexMap = {}
        for i in range(len(tupledPoints)): #label all points with an int
            pointToIndexMap[tupledPoints[i]] = i
        
        while edgeHeap and edges_used < len(points)-1: #at most n-1 edges in MST
            cost, src, dest = heapq.heappop(edgeHeap)
            srcIndex = pointToIndexMap[src]
            destIndex = pointToIndexMap[dest]
            if union(srcIndex,destIndex):
                res+=cost
                edges_used+=1
        
        return res

        #Note: Prim's is better as you dont need to calculate/store edges in this graph. 
        #Kruskal implmentation is O(n^2logn) time and O(n^2) space for building edge heap


    