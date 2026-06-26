# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #pre order
        # left side
        # visit, left, right
        
        #in order
        #bottom
        #left,visit,right

        if not inorder or not preorder: #empty input gaurd
            return None
        

        inOrderHash = {}
        for i in range(len(inorder)):
            inOrderHash[inorder[i]] = i
        
        preIndex = 0

        def builTreewithInOrderHash(left,right):
            nonlocal preIndex
            if left > right:
                return None
            
            rootVal = preorder[preIndex]
            preIndex+=1
            root = TreeNode(rootVal)
            mid = inOrderHash[rootVal]
            root.left = builTreewithInOrderHash(left, mid-1)
            root.right = builTreewithInOrderHash(mid+1, right)

            return root
        
        return builTreewithInOrderHash(0,len(inorder)-1)
        



        



            
