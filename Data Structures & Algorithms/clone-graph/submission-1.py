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
        seen = {head.val:head}
        nodeStack = [node]
        while nodeStack:
            currNode = nodeStack.pop()
            # print(currNode)
            currCopy = seen[currNode.val]
            
            currNeighbors = []
            for neighbor in currNode.neighbors:
                if neighbor.val not in seen:
                    nodeStack.append(neighbor)
                    copy = Node(neighbor.val)
                    seen[copy.val]=copy
                    currNeighbors.append(copy)
                else:
                    currNeighbors.append(seen[neighbor.val])
            currCopy.neighbors = currNeighbors

        return head
                    

