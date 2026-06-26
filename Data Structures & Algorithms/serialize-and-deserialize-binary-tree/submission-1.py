# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def maxHeightDfs(self,root):
        if not root:
            return 0
        
        leftH = self.maxHeightDfs(root.left)
        rightH = self.maxHeightDfs(root.right)

        return 1 + max(leftH, rightH)
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # #idea: build btree as array
        # #what will be size of array? max height of tree * 2 
        
        # #2*p+1
        # #2*p+2
        # height = self.maxHeightDfs(root)
        # size = 2**height
        # print(height)
        # print(2**height)

        # btreeArray = ['N'] * size
        # print(btreeArray)

        #we need to do a level order traversal where we just append in order
        allNodes = []
        q1 = deque([root])
        
        while q1:
            currLen = len(q1)
            currRes = []
            for i in range(currLen):
                
                currNode = q1.popleft()

                if not currNode:
                    currRes.append(None)
                else:
                    q1.append(currNode.left)
                    q1.append(currNode.right)
                    currRes.append(currNode.val)
                
            allNodes.append(currRes)
        
        
        # print(allNodes)

        mergedNodes = []
        for level in allNodes:
            for v in level:
                if v == None:
                    mergedNodes.append("N")
                else:
                    mergedNodes.append(str(v))
        # print(mergedNodes)
        ans = ';'.join(mergedNodes) #the semicolon repersents new value
        print(ans)
        return ans


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        bTreeArr = data.split(';')
        if not bTreeArr or bTreeArr == ["N"]:
            return None


        root = TreeNode(int(bTreeArr[0]))
        q1 = deque([root])
        i = 1 #always pointing to next node not in queue
        #need to undo BFS traversal
        while q1 and i < len(bTreeArr):
            curr = q1.popleft()

            if i < len(bTreeArr):
                if bTreeArr[i] != "N":
                    curr.left = TreeNode(int(bTreeArr[i]))
                    q1.append(curr.left)
                i+=1
            
            if i < len(bTreeArr):
                if bTreeArr[i] != "N":
                    curr.right = TreeNode(int(bTreeArr[i]))
                    q1.append(curr.right)
                i+=1
        
        return root
            








