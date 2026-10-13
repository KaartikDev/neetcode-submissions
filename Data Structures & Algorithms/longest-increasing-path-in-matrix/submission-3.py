class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #(r1,c1), (prev_row2,prev_col2) are the states
        
        memo = {}
        ROW_C = len(matrix)
        COL_C = len(matrix[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r1,c1):
            # if r1 >= ROW_C or r1 < 0:
            #     return 0
            # if c1 >= COL_C or c1 < 0:
            #     return 0
            if (r1,c1) in memo:
                return memo[(r1,c1)]
            best = 1
            for dr,dc in dirs:
                nr,nc = r1+dr,c1+dc
                if nr >= 0 and nr < ROW_C and nc >= 0 and nc < COL_C and matrix[nr][nc] > matrix[r1][c1]:
                    best = max(best,1+dfs(nr,nc))
            memo[(r1,c1)] = best
            return memo[(r1,c1)] 
        
        res = 0
        for i in range(ROW_C):
            for j in range(COL_C):
                res = max(res, dfs(i,j))
        return res


            