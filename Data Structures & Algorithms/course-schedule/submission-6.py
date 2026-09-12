# class Node:
#     # def __init__(self,val, next=None):
#     #     self.val = val
#     #     self.next = next

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

       

        dependancyMap = {}
        indegree = {}
        for a,b in prerequisites:
            #must take b before u take a
            #b -> a is the order u must take
            if b not in dependancyMap:
                dependancyMap[b] = []
                indegree[b] = 0
            if a not in dependancyMap:
                dependancyMap[a] = []
                indegree[a] = 0
            dependancyMap[b].append(a)
            indegree[a]+=1

        #some courses may be disconnected/have no pre or post reqs
        for i in range(numCourses):
            if i not in dependancyMap:
                dependancyMap[i] = []
                indegree[i] = 0

        print(dependancyMap,indegree)

        #run kahans algo for topological sort
        availableCourses = deque()
        taken = set()
        for course in indegree:
            if indegree[course] == 0:
                availableCourses.append(course)
                taken.add(course)
        
        while availableCourses:
            currCourse = availableCourses.popleft()
            for nei in dependancyMap[currCourse]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    availableCourses.append(nei)
                    taken.add(nei)
            
        return len(taken) == numCourses
        

        

