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
        origToCopy = {node:head}
        stack = [node]

        while stack:
            orig = stack.pop()
            for origNei in orig.neighbors:
                if origNei not in origToCopy:
                    origToCopy[origNei] = Node(origNei.val)
                    stack.append(origNei)

                origToCopy[orig].neighbors.append(origToCopy[origNei])
        return head
