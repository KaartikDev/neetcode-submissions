class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])
        VISTED_VAL = "#"
        def dfs(row,col):
            # print("entry=",row,col)
            if row < 0 or row >= ROW_COUNT:
                # print("OUT")
                return 0
            if col < 0 or col >= COL_COUNT:
                # print("OUT")
                return 0
            if grid[row][col] == 0 or grid[row][col] == VISTED_VAL:
                # print("Invalid")
                return 0
            

            #only other value is "1"
            # print("plus 1")
            grid[row][col] = VISTED_VAL
            upSize = dfs(row-1,col)
            downSize = dfs(row+1,col)
            leftSize = dfs(row,col-1)
            rightSize = dfs(row,col+1)

            return 1 + upSize + downSize + leftSize + rightSize
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                temp = dfs(i,j)
                # print(temp)
                count=max(temp,count)
        
        return count