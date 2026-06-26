class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])
        VISTED_VAL = "#"
        def dfs(row,col):
            if row < 0 or row >= ROW_COUNT:
                return False
            if col < 0 or col >= COL_COUNT:
                return False
            if grid[row][col] == "0" or grid[row][col] == VISTED_VAL:
                return False
            

            #only other value is "1"

            grid[row][col] = VISTED_VAL
            upSize = dfs(row-1,col)
            downSize = dfs(row+1,col)
            leftSize = dfs(row,col-1)
            rightSize = dfs(row,col+1)

            return True
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if dfs(i,j):
                    count+=1
        
        return count

        #O(n^2) time complexity buecause we vist each node at most once
