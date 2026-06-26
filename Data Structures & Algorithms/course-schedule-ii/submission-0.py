class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #this is same as before but now when we do khans algo, when we take a node indegree==0 append to res array


        def buildAdjandIndegree(V_count,E):
            adjList = []
            indegree = []

            for i in range(V_count):
                adjList.append([])
                indegree.append(0)
            
            for edge in E:
                a = edge[0]
                b = edge[1]
                adjList[b].append(a)
                indegree[a]+=1
            return adjList, indegree
        adjList,indegree = buildAdjandIndegree(numCourses,prerequisites)

        res = []
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        
        while queue:
            availableClass = queue.popleft()
            res.append(availableClass)

            for dependant in adjList[availableClass]:
                indegree[dependant]-=1
                if indegree[dependant] == 0:
                    queue.append(dependant)
        
        
        # for i in range(len(adjList)):
        #     print(i,adjList[i])
        
        if len(res) == numCourses:
            return res
        else:
            return []


