class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #do a d
        # return 1
        #brute for solution:
        #at each cell do a dfs to ensure it can get to both the (left or top) and (right or bottom)
        #O(n^2 * n^2) --> O(10000) as n<=100 for this problem for 
        

        ROW_COUNT = len(heights)
        COL_COUNT = len(heights[0])

        atlanticSet = set()
        
        
        pacificSet = set()
        
        
        def pacificDFS(row,col):

                        
            pacificSet.add((row,col))

            if (row+1,col) not in pacificSet and row+1<ROW_COUNT and heights[row][col] <= heights[row+1][col]:
                pacificDFS(row+1,col)
            if (row-1,col) not in pacificSet and row-1>=0 and heights[row][col] <= heights[row-1][col]:
                pacificDFS(row-1,col)
            if (row,col+1) not in pacificSet and col+1<COL_COUNT and heights[row][col] <= heights[row][col+1]:
                pacificDFS(row,col+1)
            if (row,col-1) not in pacificSet and col-1>=0 and heights[row][col] <= heights[row][col-1]:
                pacificDFS(row,col-1)

        def atlanticDFS(row,col):
            atlanticSet.add((row,col))

            if (row+1,col) not in atlanticSet and row+1<ROW_COUNT and heights[row][col] <= heights[row+1][col]:
                atlanticDFS(row+1,col)
            if (row-1,col) not in atlanticSet and row-1>=0 and heights[row][col] <= heights[row-1][col]:
                atlanticDFS(row-1,col)
            if (row,col+1) not in atlanticSet and col+1<COL_COUNT and heights[row][col] <= heights[row][col+1]:
                atlanticDFS(row,col+1)
            if (row,col-1) not in atlanticSet and col-1>=0 and heights[row][col] <= heights[row][col-1]:
                atlanticDFS(row,col-1)
        
        for i in range(ROW_COUNT):
            pacificDFS(i,0)
        for j in range(COL_COUNT):
            pacificDFS(0,j)
        
        for i in range(ROW_COUNT):
            atlanticDFS(i,COL_COUNT-1)
        for j in range(COL_COUNT):
            atlanticDFS(ROW_COUNT-1,j)
        
        
        # for r,c in pacificSet:
        #     pacificDFS(r,c)
        #     atlanticDFS(r,c)
        
        # print(pacificSet)
        # print(atlanticSet)
        validCells = []
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if (i,j) in pacificSet and (i,j) in atlanticSet:
                    validCells.append([i,j])
            
        return validCells

        # validList = []
        # def bfsReachBoth(row,col):
            
        #     canReachAtlantic = False
        #     canReachPacific = False

        #     queue = deque([(row,col)])
        #     seen = set((row,col))
        #     #and not (canReachAtlanti or canReachPacific)
        #     while queue:
        #         for _ in range(len(queue)):
        #             currRow,currCol = queue.popleft()
        #             if (currRow,currCol) in atlanticSet:
        #                 canReachAtlantic = True
        #             if (currRow,currCol) in pacificSet:
        #                 canReachPacific = True
                    
        #             if canReachAtlantic and canReachPacific:
        #                 validList.append([row,col])
        #                 return
                    
        #             if currRow+1<ROW_COUNT and heights[currRow][currCol] >= heights[currRow+1][currCol] and (currRow+1,currCol) not in seen:
        #                 queue.append((currRow+1,currCol))
        #                 seen.add((currRow+1,currCol))
        #             if currRow-1>=0 and heights[currRow][currCol] >= heights[currRow-1][currCol] and (currRow-1,currCol) not in seen:
        #                 queue.append((currRow-1,currCol))
        #                 seen.add((currRow-1,currCol))

        #             if currCol+1<COL_COUNT and heights[currRow][currCol] >= heights[currRow][currCol+1] and (currRow,currCol+1) not in seen:
        #                 queue.append((currRow,currCol+1))
        #                 seen.add((currRow,currCol+1))

        #             if currCol-1>=0 and heights[currRow][currCol] >= heights[currRow][currCol-1] and (currRow,currCol-1) not in seen:
        #                 queue.append((currRow,currCol-1))
        #                 seen.add((currRow,currCol-1))
            
        # for i in range(ROW_COUNT):
        #     for j in range(COL_COUNT):
        #         bfsReachBoth(i,j)
            
    
        # return -1
                    
                        








