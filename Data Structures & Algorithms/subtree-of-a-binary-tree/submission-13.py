# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
       


        
        def sameTree(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            left = sameTree(root.left,subRoot.left)
            right = sameTree(root.right,subRoot.right)
            
            # print(curr,left,right)
            return left and right
        
        #need to iterate over root now:
        def dfs(root):
            if not root:
                return False
            
            if sameTree(root,subRoot):
                return True
             
            left = dfs(root.left)
            right = dfs(root.right)

            return left or right
        
        return dfs(root)





