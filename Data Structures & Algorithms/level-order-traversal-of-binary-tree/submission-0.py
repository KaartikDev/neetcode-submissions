# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:
            return []


        q1 = deque()
        q2 = deque()
        q1.append(root)
        
        result = []
        while q1 or q2:
            currLevel = []
            

            while q1:
                curr = q1.popleft()
                currLevel.append(curr.val)
                if curr.left is not None:
                    q2.append(curr.left)

                if curr.right :
                    q2.append(curr.right)
            
            if currLevel:
                result.append(currLevel)
            
            currLevel = []

            while q2:
                curr = q2.popleft()
                currLevel.append(curr.val)
                if curr.left:
                    q1.append(curr.left)

                if curr.right:
                    q1.append(curr.right)
        
           
            if currLevel:
                result.append(currLevel)
        
        return result
           
            




            
