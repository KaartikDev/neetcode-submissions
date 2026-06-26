class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #idea:
        # run dyskstra on each chells --> O(n^4) time
        # ~(10^2)^4 --> 10^8 or 100 million iteration
        
        #idea:
        # starting from a treasure chest make nodes of touching it with one
        # nodes touchin ghrme have 2
        # then repeat until no more expansion possible
        # do same for next treasure chest and overwrite whenver new distance < saved distance

        # --> a bfs

        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])
        print(ROW_COUNT,COL_COUNT)
        # def incremetBFS(row,col,currDist):
        #     if row < 0 or row >= ROW_COUNT:
        #         return None
        #     if row > 0
        queue = deque()
        #optimiztion put all the zeros in queue first
        for row in range(ROW_COUNT):
            for col in range(COL_COUNT):
                if grid[row][col] == 0:
                    #at treasure chest store as bfs source
                    queue.append((row,col))
                    
                    # temp = 0
        
        currDist = 0
        while queue:
            for _ in range(len(queue)):
                currRow, currCol = queue.popleft()
                # print("entry row,col,dist=",currRow,currCol,grid[currRow][currCol])
                #checking 4 directions
                if currRow-1 >= 0 and grid[currRow-1][currCol] > 0 and grid[currRow-1][currCol] > currDist+1:
                    grid[currRow-1][currCol] = currDist+1
                    queue.append((currRow-1,currCol))
                                
                if currRow+1 < ROW_COUNT and grid[currRow+1][currCol] > 0 and grid[currRow+1][currCol] > currDist+1:
                    grid[currRow+1][currCol] = currDist+1
                    queue.append((currRow+1,currCol))
                            
                if currCol-1 >= 0 and grid[currRow][currCol-1] > 0 and grid[currRow][currCol-1] > currDist+1:
                    grid[currRow][currCol-1] = currDist+1
                    queue.append((currRow,currCol-1))
                if currCol+1 < COL_COUNT and grid[currRow][currCol+1] > 0 and grid[currRow][currCol+1] > currDist+1:
                    grid[currRow][currCol+1] = currDist+1
                    queue.append((currRow,currCol+1))
            currDist+=1

