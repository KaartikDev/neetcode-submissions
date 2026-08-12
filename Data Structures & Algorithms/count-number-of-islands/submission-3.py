class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])

        VISITED = "#"
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row,col):
            if row >= ROW_COUNT or row < 0:
                return False
            if col >= COL_COUNT or col < 0:
                return False
            if grid[row][col] == "0" or grid[row][col] == VISITED:
                return False

            grid[row][col] = VISITED
            
            
            for currDir in directions:
                nr, nc = row + currDir[0], col + currDir[1]
                dfs(nr,nc)
            
            return True
        res = 0
        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if dfs(r,c):
                    res+=1
        return res


