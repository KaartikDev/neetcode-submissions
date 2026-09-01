class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        bfsQueue = deque()

        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if grid[i][j] == 2:
                    bfsQueue.append((i,j))
        
        time = 0
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        while bfsQueue:
            atLeastoneRot = False
            currLen = len(bfsQueue)
            for _ in range(currLen):
                row,col = bfsQueue.popleft()
                for dr,dc in dirs:
                    nr,nc = row+dr,col+dc
                    if 0<=nr<ROW_COUNT and 0<=nc<COL_COUNT and grid[nr][nc] == 1:
                        bfsQueue.append((nr,nc))
                        atLeastoneRot = True
                        grid[nr][nc] = 2
            
            if atLeastoneRot:
                time+=1
        


        #see if any fruit still survivied
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if grid[i][j] == 1:
                    return -1
        
        #return calc time
        return time
             
                    