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

        def dfsWithHash(left,right):
            nonlocal preIndex
            if left > right:
                return None
            
            rootVal = preorder[preIndex] #the root of curr subtree is always first in preorder
            root = TreeNode(rootVal) #make curr node
            

            preIndex+=1 #increment forward BEFORE recursive calls!!

            mid = inOrderHash[rootVal] #the mid point inOrder arr splits up left and rigth subtress
            root.left = dfsWithHash(left, mid-1) #left to mid-1 is left subtree
            root.right = dfsWithHash(mid+1, right) #mid+1 to right is right subtree
            # mid is root

            return root
        
        return dfsWithHash(0,len(inorder)-1)
        



        



            
