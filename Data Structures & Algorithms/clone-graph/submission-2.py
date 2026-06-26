"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #no self loops. 
        #no duplicate edges
        
        head = Node(node.val)
        seen = {node.val:head}
        nodeStack = [node]
        while nodeStack:
            originalNode = nodeStack.pop()
            # print(currNode)
            currCopy = seen[originalNode.val]
            
            copyNeighbors = []
            for orignalNeigbor in originalNode.neighbors:
                if orignalNeigbor.val not in seen:
                    
                    copy = Node(orignalNeigbor.val)
                    seen[orignalNeigbor.val]=copy

                    nodeStack.append(orignalNeigbor)
                    copyNeighbors.append(copy)
                else:
                    copyNeighbors.append(seen[orignalNeigbor.val])
            currCopy.neighbors = copyNeighbors

        return head
                    

