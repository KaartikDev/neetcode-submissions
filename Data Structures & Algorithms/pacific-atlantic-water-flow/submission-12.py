class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        ROW_COUNT = len(heights)
        COL_COUNT = len(heights[0])

        
        
        
        
        
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

        atlanticSet = set()
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
        
        
        validCells = list(pacificSet & atlanticSet)
            
        return validCells

        #O(nm) memory, O(n*m) time compelxity (eahc cell stored and visted at msot 2n*m times) --> O(nm)