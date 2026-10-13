class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #we need to add all of the parentes...

        adjMap = {} #post -> pre

        for pre,post in prerequisites:
            if pre not in adjMap:
                adjMap[pre] = set()
            if post not in adjMap:
                adjMap[post] = set()
            adjMap[post].add(pre)

        
        #need to check if path exists vj -> uj
        #need to memo res so we can save time
        memo = {}
        def dependsOn(prereq, postreq):
            if prereq in adjMap.get(postreq,set()):
                return True
            elif (prereq,postreq) in memo:
                return memo[(prereq,postreq)]
            
            pathExists = False
            for nei in adjMap.get(postreq,set()):
                if dependsOn(prereq,nei): #we check if the prereq is "grandparent" by looking at neighbors 
                    pathExists = True
            memo[(prereq, postreq)] = pathExists
            return memo[(prereq, postreq)]
        res = []
        for uj,vj in queries:
            res.append(dependsOn(uj, vj))
        return res


