# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # do a level order BFS and search entire tree for pq, if found then true
        # O(n^2) time

        # can i do better?


        # OH ITS ORDERED, how can i take advantaged of this?
        #can now do O(nlogn) as we do BFS and at eahc level do a binary search for pq

        #maybe we can solve level like this:
            #if root.val is in between p.val and q.val (or opposite order) then we know on differnt tree sides
                #WE ON LCA
            #if root.val both >= or <= p.val and q.val, then we just move in that dir
        

        if not root: #emptry tree gaurd, something went wrong
            print("ERRROORRR")
            return None 
        #check if in between (alr LCA):
        ans = None
        if (p.val >= root.val and q.val <= root.val) or (q.val >= root.val and p.val <= root.val):
           ans = root
        elif (p.val > root.val and q.val > root.val): 
            ans = self.lowestCommonAncestor(root.right,p,q)
        elif (p.val < root.val and q.val < root.val):
            ans = self.lowestCommonAncestor(root.left,p,q)
        
        return ans
        #O(h) time complexity
        #O(h) space complexity

