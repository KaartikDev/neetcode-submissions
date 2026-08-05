class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #set row 0 and col 0 to 0 on one pass through
        #then set those entire rows/cols to zero

        #setting matrix[row][0] to zero if a zero exsits in it

        ROW_COUNT = len(matrix)
        COL_COUNT = len(matrix[0])

        zeroInLeftCol = False
        for row in range(ROW_COUNT):
            if matrix[row][0] == 0:
                zeroInLeftCol = True
        
        zeroInTopRow = False
        for col in range(COL_COUNT):
            if matrix[0][col] == 0:
                zeroInTopRow = True
        
        #now we use col 0 as bool array 
        for row in range(1,ROW_COUNT):
            foundZero = False
            for col in range(COL_COUNT):
                if matrix[row][col] == 0:
                    foundZero = True
            
            if foundZero:
                matrix[row][0] = 0
        
        #now we use row 0 as bool array 
        for col in range(1,COL_COUNT):
            foundZero = False
            for row in range(ROW_COUNT):
                if matrix[row][col] == 0:
                    foundZero = True
            
            if foundZero:
                matrix[0][col] = 0
        

        #now we update the insides (ignoring row 0 and col 0)


        # updating rows
        for row in range(1,ROW_COUNT):
            for col in range(1,COL_COUNT):
                if matrix[row][0] == 0:
                    matrix[row][col] = 0
        # update cols
        for col in range(1,COL_COUNT):
            for row in range(1,ROW_COUNT):
                if matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        #now we update row 0 and col 0
        if zeroInTopRow:
            for col in range(COL_COUNT):
                matrix[0][col] = 0
        
        if zeroInLeftCol:
            for row in range(ROW_COUNT):
                matrix[row][0] = 0
        
        




                
