class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #we need to add all of the parents

        #so if bi --> ai and later we have ci --> bi
        #this means bi depends on ai and ci depends on bi, and by deifiton ci dpeends on ai
        
        #for querries we just need to reverse this, and then check if we can traverse vj to uj.
        #Time: O(Q * (V+E)) as we do dfs for each search

        adjMap = {}
        
        for u,v in prerequisites:
            if v not in adjMap:
                adjMap[v] = []
            adjMap[v].append(u)
        
        print(adjMap)

        def dfs(start,target):
            if start == target:
                return True
            
            stack = [start]
            visited = set([start])
            while stack:
                curr = stack.pop()
                if curr == target:
                    return True
                for nei in adjMap.get(curr,[]):
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
            return False
                

        res = []
        for target, start in queries:
            res.append(dfs(start,target))
        return res

