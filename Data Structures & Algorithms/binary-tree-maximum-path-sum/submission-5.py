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
        
        res = [root.val]

        #returns max plat w/o split
        def dfs(root):
            if not root:
                return 0
            
            leftMax = max(0,dfs(root.left)) # --> ignore egative pths
            rightMax = max(0,dfs(root.right)) # --> ignore egative pths

            #check if spliting  optimal
            res[0] = max(res[0],leftMax+root.val+rightMax)

            #return max path sum
            return root.val + max(leftMax,rightMax)


        dfs(root)
        return res[0]

            
        

            