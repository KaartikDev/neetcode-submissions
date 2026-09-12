class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])
        VISITED = "#"
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r,c):
            if grid[r][c] != "1":
                return 
            grid[r][c] = VISITED
            queue = deque([(r,c)])
            while queue:
                for _ in range(len(queue)):
                    currR,currC = queue.popleft()
                    for dr,dc in dirs:
                        nr, nc = currR + dr, currC + dc
                        if nr >= 0 and nr < ROW_COUNT and nc >= 0 and nc < COL_COUNT and grid[nr][nc]=="1":
                            grid[nr][nc] = VISITED
                            queue.append((nr,nc))
        
        count = 0
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if grid[i][j] == "1":
                    # print(grid[i][j])
                    count+=1
                    bfs(i,j)
        return count
                            


        