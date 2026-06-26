class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #empty board gaurd
        

        NUM_ROWS = len(board)
        NUM_COLS = len(board[0])
        
        def dfs(row,col,k):
            # print("enter", row, col, "index =", k)

            
            if row >= NUM_ROWS or row < 0:
                return False
            if col >= NUM_COLS or col < 0:
                return False
            if board[row][col] != word[k]:
                return False
            
            if k == len(word)-1:
                return True


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
        

        #start a dfs which looks for paths upto len(word) at each cell
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = dfs(i,j,0)
                if res:
                    return res
        
        #time O(mn * mn)
        #space O(len(word))
        return False
