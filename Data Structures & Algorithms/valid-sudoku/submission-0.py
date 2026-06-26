class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # print("ROW")
        #Step 1: check all the rows row major traversal
        for row in board: #here row is a list
            countOfNumbers = 0
            rowSet = set(row)
            for col in row:
                if col.isdigit():
                    countOfNumbers+=1
            
            # print(rowSet, countOfNumbers)
            if countOfNumbers+1 != len(rowSet): #the row set should have all unique numbers + 1 for the '.' empty space
                return False
        
        # print("COL")
        #Step 2 check all the cols col major traversal
        for row in range(len(board)):
            countOfNumbers = 0
            colSet = set()
            for col in range(len(board)): #here row is a numebr
                colSet.add(board[col][row])
                if board[col][row].isdigit():
                    countOfNumbers+=1
            
            # print(colSet, countOfNumbers)
            if countOfNumbers+1 != len(colSet): #the col set should have all unique numbers + 1 for the '.' empty space
                return False
        
        # print("GRID")
        #Step 3 the 3x3 grid
        horizontalInd = 0
        verticalInd = 0
        while verticalInd < len(board):
            while horizontalInd < len(board):
                countOfNumbers = 0
                gridSet = set()
                
                for row in range(3): #contruct grid set (check 3x3)
                    for col in range(3):
                        # print(board[row+verticalInd][col+horizontalInd])
                        gridSet.add(board[row+verticalInd][col+horizontalInd])
                        if board[row+verticalInd][col+horizontalInd].isdigit():
                            countOfNumbers+=1
                
                 
                if countOfNumbers+1 != len(gridSet): #the grid set should have all unique numbers + 1 for the '.' empty space
                    return False
                horizontalInd += 3
            verticalInd += 3
        
        #If passed all checks
        return True
