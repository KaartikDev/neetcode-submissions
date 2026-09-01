class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                board[r][c] = "#"
                for dr,dc in dirs:
                    dfs(r+dr,c+dc)
        
        for i in range(ROWS):
            dfs(i,0)
            dfs(i,COLS-1)
        for j in range(COLS):
            dfs(0,j)
            dfs(ROWS-1,j)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
        
        # return board