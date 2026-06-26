# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBSTwithLandR(self,root,left,right):
        if not root:
            return True
        
        if left >= root.val or root.val >= right:
            return False
        
        leftVal = self.isValidBSTwithLandR(root.left,left,root.val)
        rightVal = self.isValidBSTwithLandR(root.right,root.val,right)
        
        return leftVal and rightVal


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isValidBSTwithLandR(root,float('-inf'),float('inf'))