# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftBound = -float("inf")
        rightBound = float("inf")
        
        st = [(root,leftBound,rightBound)]

        while st:
            curr, currLeft, currRight = st.pop()
            # print(curr.val,currLeft,currRight)
            if curr.val <= currLeft or curr.val >= currRight:
                return False
            
            if curr.left:
                st.append([curr.left,currLeft,curr.val])
            if curr.right:
                st.append([curr.right,curr.val,currRight])
        return True

