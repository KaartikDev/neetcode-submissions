# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def depthTree(self, root):
    #     if not root:
    #         return 0
    #     leftH = self.depthTree(root.left)
    #     rightH = self.depthTree(root.right)
    #     return 1 + max(leftH, rightH)
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     left = self.diameterOfBinaryTree(root.left)
    #     right = self.diameterOfBinaryTree(root.right)
    #     leftH = self.depthTree(root.left)
    #     rightH = self.depthTree(root.right)
    #     return max(leftH+rightH,left,right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        #key idea: either we can:
        # "split" at a node and sum its left and right as total path diameter
        # OR we can add its MAX height to current path diameter

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            res[0] = max(left+right,res[0])
            return 1+max(left,right)
        
        dfs(root)
        return res[0]

        