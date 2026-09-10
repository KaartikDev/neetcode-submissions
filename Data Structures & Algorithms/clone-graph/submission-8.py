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
        origToCopyMap = {node:head}

        queue = deque([node])

        while queue:
            orignal = queue.popleft()
            copy = origToCopyMap[orignal]
            for origNei in orignal.neighbors:
                if origNei not in origToCopyMap:
                    origToCopyMap[origNei] = Node(origNei.val)
                    queue.append(origNei)
                
                copy.neighbors.append(origToCopyMap[origNei])

        return head



