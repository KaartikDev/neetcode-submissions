# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we do level order traversal and only print the right most node
        if not root:
            return []
        
        levels = []
        q = deque([root])
        
        while q:
            currLevel = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                currLevel.append(curr.val)
            levels.append(currLevel)
        # print(levels)
        res = []
        for lvl in levels:
            res.append(lvl[-1])
        
        return res