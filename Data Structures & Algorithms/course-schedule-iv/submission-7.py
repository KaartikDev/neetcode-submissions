class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #we need to add all of the parents

        #so if bi --> ai and later we have ci --> bi
        #this means bi depends on ai and ci depends on bi, and by deifiton ci dpeends on ai
        
        #for querries we just need to reverse this, and then check if we can traverse vj to uj.
        #Time: O(Q * (V+E)) as we do dfs for each search
        #Idea: use dp top down
        adjMap = {}
        
        for u,v in prerequisites:
            if v not in adjMap:
                adjMap[v] = []
            adjMap[v].append(u)
        
        print(adjMap)
        memo = {}
        def dependsOn(u,v):
            if (u,v) in memo:
                return memo[(u,v)]
            
            for prereq in adjMap.get(u,[]):
                if prereq == v or dependsOn(prereq,v):
                    memo[(u,v)] = True
                    return True
                
            memo[(u,v)] = False
            return False
                
        
        res = []
        for target, start in queries:
            res.append(dependsOn(start,target))
        # print(memo)
        return res

