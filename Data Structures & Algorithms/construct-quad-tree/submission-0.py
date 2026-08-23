"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        
        def dfs(n,r,c):
        
            if n==0:
                return None

            if n == 1:
                return Node(val = grid[r][c]==1, isLeaf=True)
            
            vals = set()
            for i in range(r,r+n):
                for j in range(c,c+n):
                    vals.add(grid[i][j])
            
            if len(vals) == 1:
                return Node(val= grid[r][c]==1 ,isLeaf=True)
            
            #more than one value in gird --> not leaf
            currIsLeaf = False
            currVal = False #can be anything
            newSideLen = n//2 #n is gaurnteed to be power of 2

            #copy grid as u pass it down so slicing still works
            topLeft = dfs(newSideLen,r,c)
            topRight = dfs(newSideLen,r,c+newSideLen)

            bottomLeft = dfs(newSideLen,r+newSideLen,c)
            bottomRight = dfs(newSideLen,r+newSideLen,c+newSideLen)

            return Node(val=currVal, isLeaf=currIsLeaf, topLeft=topLeft,
             topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)
        return dfs(len(grid),0,0)


        
 






