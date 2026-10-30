# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftMax = max(0,dfs(root.left))
            rightMax = max(0,dfs(root.right))

            res[0] = max(res[0],leftMax+root.val+rightMax) #we split
            return root.val+max(rightMax,leftMax) #We continue
        dfs(root)
        return res[0]
            