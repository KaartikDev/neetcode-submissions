class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #starting from all border "O", mark them as "#" via dfs
        #then iterate through array marking remaining "O" as "X"
        #convert "#" back to "O"

        #stage 1 border dfs
        ROW_COUNT = len(board)
        COL_COUNT = len(board[0])

        

        def dfs(row,col):
            if row >= ROW_COUNT or row < 0:
                return None
            if col >= COL_COUNT or col < 0:
                return None
            if board[row][col] == "#" or board[row][col] == "X":
                return None
            
            if board[row][col] == "O":
                board[row][col] = "#"
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)
        
        for i in range(ROW_COUNT):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][COL_COUNT-1] == "O":
                dfs(i,COL_COUNT-1)
        
        for j in range(COL_COUNT):
            if board[0][j] == "O":
                dfs(0,j)
            if board[ROW_COUNT-1][j] == "O":
                dfs(ROW_COUNT-1,j)
        
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if board[i][j] == "#":
                    board[i][j] = "O"
        
        #O(n^2) time compelxity, O(n^2) space compelxity

