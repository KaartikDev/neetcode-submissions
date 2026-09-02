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



        head = Node(node.val)
        orignalToCopyMap = {node:head}
        stack = [node]
        while stack:
            origNode = stack.pop()
            copyNode = orignalToCopyMap[origNode]

            copyNeighbors = []
            for origNei in origNode.neighbors:
                
                if origNei not in orignalToCopyMap:
                    copy = Node(origNei.val)
                    orignalToCopyMap[origNei] = copy
                    copyNeighbors.append(copy)
                    stack.append(origNei)
                else:
                    copy = orignalToCopyMap[origNei]
                    copyNeighbors.append(copy)
            copyNode.neighbors = copyNeighbors
        return head
                    
                    




             