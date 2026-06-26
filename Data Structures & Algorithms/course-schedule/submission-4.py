# class Node:
#     # def __init__(self,val, next=None):
#     #     self.val = val
#     #     self.next = next

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dependancy graph need to check for cycles


        if numCourses <= 1:
            return True
        
        #build directed adjaceny list and indegree counts
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
    
        #now check indegree of all vertexes is eventually zero
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        numberOfAvailableClasses = 0

        while queue:
            #for a node with indegree zero
            #delete it and decree indegree counts of remaining
            prereq = queue.popleft()
            numberOfAvailableClasses+=1

            for dependant in adjList[prereq]:
                inDegree[dependant] -= 1
                if inDegree[dependant] == 0:
                    queue.append(dependant)
        
        return numberOfAvailableClasses == numCourses

