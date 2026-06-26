# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

            
   
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #so we can either have best path that ENDS at this node
        #or we can have best path that goes theough both left and right
        
        assert root, "no empty trees allowed"
        
        res = root.val

        #returns max plat w/o split
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            leftMax = max(dfs(root.left),0) #if entire left path sum is negative max is zero as choose none
            rightMax = max(dfs(root.right),0) 

            #compute max path WITH A SPLIT
            split_sum =root.val + leftMax + rightMax
            res = max(split_sum,res)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res

            
        

            