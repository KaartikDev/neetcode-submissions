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
            if 0 <= r < ROW_COUNT and 0 <= c < COL_COUNT and (r,c) not in seen:
                return True
            else:
                return False
        
        while len(res) != ROW_COUNT*COL_COUNT:
            res.append(matrix[r][c])
            seen.add((r,c))

            nr,nc = r+dirs[dirIndex][0],c+dirs[dirIndex][1]
            dirChangeAttempt = 0
            while not legalMove(nr,nc) and dirChangeAttempt < 3: #check the other 3 directions
                dirIndex = (dirIndex+1) % 4
                nr,nc = r+dirs[dirIndex][0],c+dirs[dirIndex][1]
                dirChangeAttempt+=1
            
            r,c = nr,nc #update r,c
        
        return res
            

