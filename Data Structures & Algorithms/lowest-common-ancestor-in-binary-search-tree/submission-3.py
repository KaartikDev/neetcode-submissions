# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
       #if both are smaller then curr then we go left
       #if both are bigger then curr then we go right
       #if on opposite sides we win

        def dfs(root):
            if not root:
                return None
            if p.val < root.val and q.val <root.val:
                return dfs(root.left)
            elif p.val > root.val and q.val>root.val:
                return dfs(root.right)
            else:
                return root
        return dfs(root)

 