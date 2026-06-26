class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #do a d
        # return 1
        #brute for solution:
        #at each cell do a dfs to ensure it can get to both the (left or top) and (right or bottom)
        #O(n^2 * n^2) --> O(10000) as n<=100 for this problem for 


        validPoints = {}

        

        ROW_COUNT = len(heights)
        COL_COUNT = len(heights[0])

        atlanticSet = set()
        for i in range(ROW_COUNT):
            atlanticSet.add((i,COL_COUNT-1))
        for j in range(COL_COUNT):
            atlanticSet.add((ROW_COUNT-1,j))
        
        pacificSet = set()
        for i in range(ROW_COUNT):
            pacificSet.add((i,0))
        for j in range(COL_COUNT):
            pacificSet.add((0,j))
        
        validList = []
        def bfsReachBoth(row,col):
            
            canReachAtlantic = False
            canReachPacific = False

            queue = deque([(row,col)])
            seen = set((row,col))
            #and not (canReachAtlanti or canReachPacific)
            while queue:
                for _ in range(len(queue)):
                    currRow,currCol = queue.popleft()
                    if (currRow,currCol) in atlanticSet:
                        canReachAtlantic = True
                    if (currRow,currCol) in pacificSet:
                        canReachPacific = True
                    
                    if canReachAtlantic and canReachPacific:
                        validList.append([row,col])
                        return
                    
                    if currRow+1<ROW_COUNT and heights[currRow][currCol] >= heights[currRow+1][currCol] and (currRow+1,currCol) not in seen:
                        queue.append((currRow+1,currCol))
                        seen.add((currRow+1,currCol))
                    if currRow-1>=0 and heights[currRow][currCol] >= heights[currRow-1][currCol] and (currRow-1,currCol) not in seen:
                        queue.append((currRow-1,currCol))
                        seen.add((currRow-1,currCol))

                    if currCol+1<COL_COUNT and heights[currRow][currCol] >= heights[currRow][currCol+1] and (currRow,currCol+1) not in seen:
                        queue.append((currRow,currCol+1))
                        seen.add((currRow,currCol+1))

                    if currCol-1>=0 and heights[currRow][currCol] >= heights[currRow][currCol-1] and (currRow,currCol-1) not in seen:
                        queue.append((currRow,currCol-1))
                        seen.add((currRow,currCol-1))
            
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                bfsReachBoth(i,j)
            
    
        return validList
                    
                        








