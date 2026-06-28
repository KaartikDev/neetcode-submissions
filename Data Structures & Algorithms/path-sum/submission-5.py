# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        def dfs(root,currSum):
            if not root.left and not root.right:
                return currSum+root.val == targetSum
            
            left = False
            if root.left:
                left = dfs(root.left,currSum+root.val)
            right = False
            if root.right:
                right = dfs(root.right,currSum+root.val)

            return left or right
        
        return dfs(root,0)
