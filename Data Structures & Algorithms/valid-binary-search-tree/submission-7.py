# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBSTwithLandR(self,root,leftBound,rightBound):
        if not root:
            return True
        
        if leftBound >= root.val or root.val >= rightBound:
            return False
        
        #update valid range to be (leftBound,curr.val) exclusive
        leftVal = self.isValidBSTwithLandR(root.left,leftBound,root.val)
        #update valid range to be (curr.val,rightBound) exclusive
        rightVal = self.isValidBSTwithLandR(root.right,root.val,rightBound)
        
        return leftVal and rightVal


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isValidBSTwithLandR(root,float('-inf'),float('inf'))