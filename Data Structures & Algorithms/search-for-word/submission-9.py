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


            if row >= NUM_ROWS or row < 0:
                return False
            if col >= NUM_COLS or col < 0:
                return False
            if len(cur) > len(word):
                return False
            if len(cur) == len(word):
                return ("".join(cur) == word)

            
            if board[row][col] != word[len(cur)]:
                return False
            
            cur.append(board[row][col])
            board[row][col] = "#" 
            used = True
            
            if len(cur) == len(word):
                return ("".join(cur) == word)
            
            ans = False
            ans = ans or dfs(row+1,col)
            ans = ans or dfs(row-1,col)
            ans = ans or dfs(row,col+1)
            ans = ans or dfs(row,col-1)
            
            #undo seen
            board[row][col] = cur.pop()

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
