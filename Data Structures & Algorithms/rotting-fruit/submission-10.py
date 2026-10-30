class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])


        # multisource bfs
        freshCount = 0
        q = deque([])
        # visited = set()

        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):
                if grid[r][c] == 1:
                    freshCount+=1
                if grid[r][c] == 2:
                    q.append((r,c))
                    # visited.add((r,c))
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        time = 0
        while q and freshCount != 0:
            time+=1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    if 0<=r+dr<ROW_COUNT and 0<=c+dc<COL_COUNT and grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        freshCount-=1
                        q.append((r+dr,c+dc))
        return time if freshCount == 0 else -1
                



