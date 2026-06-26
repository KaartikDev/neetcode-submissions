# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthTree(self, root):
        if not root:
            return 0
        leftH = self.depthTree(root.left)
        rightH = self.depthTree(root.right)
        return 1 + max(leftH, rightH)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        leftH = self.depthTree(root.left)
        rightH = self.depthTree(root.right)
        return max(leftH+rightH,left,right)
        