class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #this is a weird form of dfs
        res = []
        seen = set()
        ROW_COUNT = len(matrix)
        COL_COUNT = len(matrix[0])

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        dirIndex = 0

        r,c = 0,0

        def legalMove(r,c):
            if r < 0 or nr >= ROW_COUNT or c < 0 or c >= COL_COUNT or (r,c) in seen:
                return False
            else:
                return True
        
        while len(res) != ROW_COUNT*COL_COUNT:
            res.append(matrix[r][c])
            seen.add((r,c))

            nr,nc = r+dirs[dirIndex][0],c+dirs[dirIndex][1]
            
            dirFindingCount = 0
            while not legalMove(nr,nc) and dirFindingCount < 4:
                dirIndex = (dirIndex+1) % 4
                nr,nc = r+dirs[dirIndex][0],c+dirs[dirIndex][1]
                dirFindingCount+=1
            
            r,c = nr,nc
        
        return res
            

