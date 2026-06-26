# class Node:
#     # def __init__(self,val, next=None):
#     #     self.val = val
#     #     self.next = next

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dependancy graph need to check for cycles


        if numCourses <= 1:
            return True
        
        #self edge
        #build adjaceny list
        def buildAdjandIndegree(V:int,E: List[List[int]]):
            adj = []
            indegrees = []
            for _ in range(V):
                adj.append([])
                indegrees.append(0)
            
            for edge in E:
                u = edge[0]
                v = edge[1]
                adj[v].append(u)
                indegrees[u]+=1
                
            return (adj,indegrees)
        
    
        adjList,inDegree = buildAdjandIndegree(numCourses,prerequisites)
    
        #now do check indegree of all vertexes
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        taken = 0

        while queue:
            #for a node with indegree zero
            #delete it and decree indegree counts of remaining
            u = queue.popleft()
            taken+=1

            for neighbor in adjList[u]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return taken == numCourses

