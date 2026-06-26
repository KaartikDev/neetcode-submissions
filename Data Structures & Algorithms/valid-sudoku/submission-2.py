class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # print("ROW")
        #Step 1: check all the rows row major traversal
        for row in board: #here row is a list
            countOfNumbers = 0
            rowSet = set()
            for col in row: #col is element in row list
                if col.isdigit():
                    rowSet.add(col)
                    countOfNumbers+=1
            
            # print(rowSet, countOfNumbers)
            if countOfNumbers != len(rowSet): #the row set should have all unique numbers + 1 for the '.' empty space
                return False
        
        # print("COL")
        #Step 2 check all the cols col major traversal
        for row in range(len(board)):
            countOfNumbers = 0
            colSet = set()
            for col in range(len(board)): #here row is a index
                if board[col][row].isdigit():
                    colSet.add(board[col][row])
                    countOfNumbers+=1
            
            # print(colSet, countOfNumbers)
            if countOfNumbers != len(colSet): #the col set should have all unique numbers 
                return False
        
        # print("GRID")
        #Step 3 the 3x3 grid
        
        verticalInd = 0
        while verticalInd < len(board):
            horizontalInd = 0
            while horizontalInd < len(board):
                countOfNumbers = 0
                gridSet = set()
                
                for row in range(3): #contruct grid set (check 3x3)
                    for col in range(3):
                        # print(board[row+verticalInd][col+horizontalInd])
                        
                        if board[row+verticalInd][col+horizontalInd].isdigit():
                            countOfNumbers+=1
                            gridSet.add(board[row+verticalInd][col+horizontalInd])
                
                 
                if countOfNumbers != len(gridSet): #the grid set should have all unique numbers + 1 for the '.' empty space
                    return False
                horizontalInd += 3
            verticalInd += 3
        
        #If passed all checks
        return True
