class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #run dijsktras
        #edge wieght is delta between curr and next
        #(0,0) to (row-1,col-1)

        #note this is looking to minimize the max edge weight in a path, not total path len

        ROW_COUNT = len(heights)
        COL_COUNT = len(heights[0])
        DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

        temp = [float('inf') for _ in range(COL_COUNT)]
        efforts = [temp.copy() for _ in range(ROW_COUNT)]
        print(heights)
        print(efforts)

        
        efforts[0][0] = 0
        pq = []

        
        heapq.heappush(pq,(0,(0,0))) # distance, (x,y)
        while pq:
            currEff, currNode = heapq.heappop(pq)
            r,c = currNode[0],currNode[1]
            if currEff > efforts[r][c]:
                continue
            
            for dr,dc in DIRS:
                nr,nc=r+dr,c+dc
                if nr < 0 or nr >= ROW_COUNT or nc < 0 or nc >= COL_COUNT:
                    continue
                nextEffort = max(currEff,abs(heights[r][c] - heights[nr][nc]))
                
                if nextEffort < efforts[nr][nc]:
                    efforts[nr][nc] = nextEffort
                    heapq.heappush(pq,(nextEffort,(nr,nc)))
        
        print(efforts)

        return efforts[ROW_COUNT-1][COL_COUNT-1]
            



