class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #emty board gaurd

        

        NUM_ROWS = len(board)
        NUM_COLS = len(board[0])
        
        def dfs(row,col,k):
            # print("enter", row, col, "index =", k)

            if k == len(word):
                return True
            
            if row >= NUM_ROWS or row < 0:
                return False
            if col >= NUM_COLS or col < 0:
                return False
            if board[row][col] != word[k]:
                return False


            saved = board[row][col]
            board[row][col] = "#" #mark curr as seen
            
            
            ans = False
            ans = ans or dfs(row+1,col,k+1)
            ans = ans or dfs(row-1,col,k+1)
            ans = ans or dfs(row,col+1,k+1)
            ans = ans or dfs(row,col-1,k+1)
            
            #undo seen
            board[row][col] = saved

            return ans
        


        for i in range(len(board)):
            for j in range(len(board[i])):
                res = dfs(i,j,0)
                if res:
                    return res
        
        return False
