# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrderCount = [0]
        def dfs(root):

            if not root:
                return None
            
            leftAns = dfs(root.left)
            # print("proc",root.val,inOrderCount)
            inOrderCount[0]+=1
            if inOrderCount[0] == k:
                return root.val
            rightAns = dfs(root.right)

            return leftAns if leftAns is not None else rightAns

        # dfs(root) 
        # print(inOrderVals, len(inOrderVals))
        #k is zero indexed
        return dfs(root)