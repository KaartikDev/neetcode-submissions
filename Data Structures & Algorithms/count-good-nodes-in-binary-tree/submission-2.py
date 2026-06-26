# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurDFSwithMax(self,root, maxSeen):
        if not root:
            return 0
        #increase count if we find a new max
        count = 0
        if root.val >= maxSeen:
            maxSeen = root.val
            count+=1
        #check leftside with new max
        count += self.recurDFSwithMax(root.left,maxSeen)
        #check rightside with same new max
        count += self.recurDFSwithMax(root.right,maxSeen)

        #return count 
        return count 

    def goodNodes(self, root: TreeNode) -> int:
        #DFS seems like the way to go...
        #need to carry maxSeen with DFS
        return self.recurDFSwithMax(root, -float('inf'))

        
        