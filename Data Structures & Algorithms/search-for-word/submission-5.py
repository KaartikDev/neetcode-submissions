class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #emty board gaurd
        if len(board) == 0:
            return False
        
        #single baord char
        if len(board) == 1:
            if len(board[0]) == 1:
                return board[0][0] == word
        
        cur = []

        NUM_ROWS = len(board)
        NUM_COLS = len(board[0])
        
        def dfs(row,col):
            # print("enter", row, col, "cur =", cur)


            if row >= NUM_ROWS:
                return False
            if col >= NUM_COLS:
                return False
            if len(cur) > len(word):
                return False
            if len(cur) == len(word):
                return ("".join(cur) == word)

            used = False
            
            if board[row][col] == "#" or board[row][col] != word[len(cur)]:
                return False
            else:
                cur.append(board[row][col])
                board[row][col] = "#"
                used = True
            
            if len(cur) == len(word):
                return ("".join(cur) == word)
            
            ans = False
            if row+1 < NUM_ROWS: #check down
                ans = ans or dfs(row+1,col)
            if row-1 >= 0: #check up
                ans = ans or dfs(row-1,col)
            if col+1 < NUM_COLS: #check right
                ans = ans or dfs(row,col+1)
            if col-1 >= 0: #check left
                ans = ans or dfs(row,col-1)
            
            if used:
                board[row][col] = cur.pop()
            else:
                cur.pop()

            return ans
        
        res = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = dfs(i,j)
                if res:
                    break
            if res:
                break
        

        return res
