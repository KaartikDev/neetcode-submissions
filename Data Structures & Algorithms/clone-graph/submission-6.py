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
        queue = deque([node])
        
        #now i want to try bfs version
        while queue:
            currLevelSize = len(queue)
            for _ in range(currLevelSize):
                original = queue.popleft()
                copy = orignalToCopyMap[original]

                for orignalNei in original.neighbors:
                    #make the node in map if unseen
                    if orignalNei not in orignalToCopyMap:
                        copyNei = Node(orignalNei.val)
                        orignalToCopyMap[orignalNei] = copyNei
                        queue.append(orignalNei) #NOTE: only add unseen nodes!! (else cycle fails)
                    
                    # add to current copy
                    copy.neighbors.append(orignalToCopyMap[orignalNei])
        return head
        
        
                    
                    




             