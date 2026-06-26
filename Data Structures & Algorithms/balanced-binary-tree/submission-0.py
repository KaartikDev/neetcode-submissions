# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: #empty tree gaurd
            return True
        
        stack = [root]
        nodeMap = {None:0} #Node : (right height, left height)
        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in nodeMap:
                stack.append(curr.left)
            elif curr.right and curr.right not in nodeMap:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                leftH = nodeMap[curr.left]
                rightH = nodeMap[curr.right]
                if abs(leftH-rightH) > 1:
                    return False
                nodeMap[curr] = 1+max(leftH,rightH)
        
        return True
