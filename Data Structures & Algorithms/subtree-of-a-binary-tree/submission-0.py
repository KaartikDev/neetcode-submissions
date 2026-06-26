# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #both roots are none its the same
            return True
        elif not p: #only p is none
            return False
        elif not q: #only q is none
            return False
        
        if p.val != q.val:
            return False
        
        leftAns = self.isSameTree(p.left,q.left)
        rightAns = self.isSameTree(p.right,q.right)
        
        return leftAns and rightAns
        #O(n) time complexity
        #O(h) space complexity

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # do we need to look for entire subtree at every node?
        if not root:
            return root == subRoot

        checkLeft = self.isSubtree(root.left,subRoot)
        checkRight = self.isSubtree(root.right,subRoot)
        ans = False
        if root and root.val==subRoot.val:
            if (self.isSameTree(root,subRoot)):
                ans = True
        return ans or checkLeft or checkRight
        #O(n^2) sol
        









