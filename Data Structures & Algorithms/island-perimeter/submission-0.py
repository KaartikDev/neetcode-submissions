class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimCount = [0]
        visited = "#"

        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= ROW_COUNT:
                return
            if c < 0 or c >= COL_COUNT:
                return
            if grid[r][c] != 1:
                return
            
            #check north,south,east,west for perim boost
            if r-1 < 0 or grid[r-1][c] == 0:
                perimCount[0]+=1
            
            if r+1 >= (ROW_COUNT) or grid[r+1][c] == 0:
                perimCount[0]+=1
            
            if c-1 < 0 or grid[r][c-1] == 0:
                perimCount[0]+=1
            
            if c+1 >= (COL_COUNT) or grid[r][c+1] == 0:
                perimCount[0]+=1
            
            grid[r][c] = visited
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if grid[i][j] == 1:
                    dfs(i,j)
        
        return perimCount[0]
         
