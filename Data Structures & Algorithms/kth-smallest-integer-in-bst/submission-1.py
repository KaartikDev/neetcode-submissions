# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrderVals = []

        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            inOrderVals.append(root.val)
            dfs(root.right)
            return None
        dfs(root)
        # print(inOrderVals, len(inOrderVals))
        #k is zero indexed
        return inOrderVals[k-1]