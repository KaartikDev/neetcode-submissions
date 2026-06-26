# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        if not root.right and not root.left: #stop at leaf nodes
            return root
        past_left = self.invertTree(root.left)
        past_right = self.invertTree(root.right)
        root.right = past_left
        root.left = past_right
        return root 

