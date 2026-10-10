# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        #stack based dfs w/ max
        if not root:
            return 0
        
        st = [(root,root.val)] #node, max seen
        good = 0
        while st:
            curr,maxSeen = st.pop()
            # print(curr.val,curr.left,curr.right)
            if curr.val >= maxSeen:
                good+=1
            
            if curr.left:
                leftMaxSeen = max(curr.left.val,maxSeen)
                st.append((curr.left,leftMaxSeen))
            if curr.right:
                rightMaxSeen = max(curr.right.val,maxSeen)
                st.append((curr.right,rightMaxSeen))
        return good

        
        