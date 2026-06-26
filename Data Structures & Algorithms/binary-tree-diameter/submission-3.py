# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def depthTree(self, root):
    #     if not root:
    #         return 0
    #     leftH = self.depthTree(root.left)
    #     rightH = self.depthTree(root.right)
    #     return 1 + max(leftH, rightH)
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     left = self.diameterOfBinaryTree(root.left)
    #     right = self.diameterOfBinaryTree(root.right)
    #     leftH = self.depthTree(root.left)
    #     rightH = self.depthTree(root.right)
    #     return max(leftH+rightH,left,right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        nodeMap = {None:(0,0)}#of shape Node pointer : (height,diameter)
        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in nodeMap:
                stack.append(curr.left)
            elif curr.right and curr.right not in nodeMap:
                stack.append(curr.right)
            else:
                curr = stack.pop() #process bottom most unknown node
                leftH, leftD = nodeMap[curr.left] #assign (0,0) no left child OR recall
                rightH,rightD = nodeMap[curr.right] #assign (0,0) no right child OR recall
                maxH = 1+ max(leftH,rightH) #calc curr
                maxD = max(leftH+rightH,leftD,rightD) 
                nodeMap[curr] = (maxH,maxD) #update map
        return nodeMap[root][1]


        