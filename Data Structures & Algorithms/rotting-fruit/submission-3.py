class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi source bfs again until all remaing fresh fruits gone

        #have fresh fruit set, whenevr rotten remove it
        #if at any point bfs stops but frsh fruits remain, return -1
        #else reutrn iterations of bfs

        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])
        SEEN_MARKER = 2
        freshFruitSet = set()
        bfsQueue = deque()
        
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if grid[i][j] == 1:
                    freshFruitSet.add((i,j))
                if grid[i][j] == 2:
                    bfsQueue.append((i,j))
        #without any time passing there is no fresh fruits AND no rotten fruiits
        # print(len(bfsQueue),len(freshFruitSet))
        
        if len(freshFruitSet) == 0:
            return 0
        
        #do bfs
        time = 0
        while bfsQueue:
            levelLength = len(bfsQueue)
            for _ in range(levelLength):
                currRow, currCol = bfsQueue.popleft()
                
                #check top and bottom
                if currRow-1 >= 0 and grid[currRow-1][currCol] == 1:
                    freshFruitSet.remove((currRow-1,currCol))
                    grid[currRow-1][currCol] = 2
                    bfsQueue.append((currRow-1,currCol))
                
                if currRow+1 < ROW_COUNT and grid[currRow+1][currCol] == 1:
                    freshFruitSet.remove((currRow+1,currCol))
                    grid[currRow+1][currCol] = 2
                    bfsQueue.append((currRow+1,currCol))
                
                #check left and right
                if currCol-1 >= 0 and grid[currRow][currCol-1] == 1:
                    freshFruitSet.remove((currRow,currCol-1))
                    grid[currRow][currCol-1] = 2
                    bfsQueue.append((currRow,currCol-1))
                
                if currCol+1 < COL_COUNT and grid[currRow][currCol+1] == 1:
                    freshFruitSet.remove((currRow,currCol+1))
                    grid[currRow][currCol+1] = 2
                    bfsQueue.append((currRow,currCol+1))
            time+=1
        
        if len(freshFruitSet) > 0:
            return -1
        else:
            return time-1




        