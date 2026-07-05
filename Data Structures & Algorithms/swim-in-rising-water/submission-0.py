class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #find path form 0,0 to n-1,n-1 which has min max edge weight
        #some sort of modfied dijsktras where cost is tracked by max edge weight instead of sum
        
        distGrid = []
        n = len(grid)
        for row in range(n):
            distGrid.append([float('inf') for i in range(n)]) #squre grid
        
        # print(distGrid)
        # minHeight = 
        distGrid[n-1][n-1] = grid[n-1][n-1]
        pq = [(distGrid[n-1][n-1],(n-1,n-1))]
        heapq.heapify(pq)
        while pq:
            currDist, pos = heapq.heappop(pq)
            currRow,currCol = pos
            if currDist > distGrid[currRow][currCol]:
                continue
            
            if currRow-1>=0:
                neigborMaxHeight = max(currDist,grid[currRow-1][currCol])
                if neigborMaxHeight < distGrid[currRow-1][currCol]:
                    distGrid[currRow-1][currCol] = neigborMaxHeight
                    heapq.heappush(pq, (neigborMaxHeight, (currRow-1,currCol)))
            
            if currRow+1<n:
                neigborMaxHeight = max(currDist,grid[currRow+1][currCol])
                if neigborMaxHeight < distGrid[currRow+1][currCol]:
                    distGrid[currRow+1][currCol] = neigborMaxHeight
                    heapq.heappush(pq, (neigborMaxHeight, (currRow+1,currCol)))

            if currCol-1>=0:
                neigborMaxHeight = max(currDist,grid[currRow][currCol-1])
                if neigborMaxHeight < distGrid[currRow][currCol-1]:
                    distGrid[currRow][currCol-1] = neigborMaxHeight
                    heapq.heappush(pq, (neigborMaxHeight, (currRow,currCol-1)))
            
            if currCol+1<n:
                neigborMaxHeight = max(currDist,grid[currRow][currCol+1])
                if neigborMaxHeight < distGrid[currRow][currCol+1]:
                    distGrid[currRow][currCol+1] = neigborMaxHeight
                    heapq.heappush(pq, (neigborMaxHeight, (currRow,currCol+1)))
        
        # print(distGrid)
        return distGrid[0][0]

