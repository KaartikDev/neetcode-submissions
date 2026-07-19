class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #(r1,c1), (prev_row2,prev_col2) are the states
        if matrix == [] or matrix == [[]]:
            return 0

        ROW_COUNT, COL_COUNT = len(matrix),len(matrix[0])
        
        memo = {}

        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            
            best = 1
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_r, next_c = r+dr, c+dc
                if 0 <= next_r < ROW_COUNT and 0 <= next_c < COL_COUNT and matrix[next_r][next_c] > matrix[r][c]:
                    best = max(best,1+dfs(next_r,next_c))
            memo[(r,c)] = best
            return memo[(r,c)]

        ans = 0
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                ans = max(ans,dfs(i,j))
        return ans


