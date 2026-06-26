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
        
        nodeQueue = deque([root])
        allNodeVals = []
        while nodeQueue:
            currVals = []
            currLen = len(nodeQueue)
            nextLen = 0
            for i in range(currLen):
                assert nodeQueue, "something went wrong empty queue in for loop"
                curr = nodeQueue.popleft()
                # print(curr.val)
                currVals.append(curr.val)
                if curr.left:
                    nextLen+=1
                    nodeQueue.append(curr.left)
                if curr.right:
                    nextLen+=1
                    nodeQueue.append(curr.right)
            allNodeVals.append(currVals)
        
        # print(allNodeVals)
        rightMost = []
        for level in allNodeVals:
            rightMost.append(level[-1])
        return rightMost