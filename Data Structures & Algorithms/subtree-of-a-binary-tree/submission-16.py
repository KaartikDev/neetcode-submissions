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
        

        def isSameTree(r1,r2):
            if not r1 and not r2:
                return True
            elif not r1:
                return False
            elif not r2:
                return False
            
            if r1.val != r2.val:
                return False
            
            left = isSameTree(r1.left,r2.left)
            right = isSameTree(r1.right,r2.right)

            return left and right
        
        st = [root]
        # seen = set(root)


        while st:
            curr = st.pop()
            
            if curr.left:
                st.append(curr.left)
            if curr.right:
                st.append(curr.right)

            if isSameTree(curr,subRoot):
                return True
        
        return False
