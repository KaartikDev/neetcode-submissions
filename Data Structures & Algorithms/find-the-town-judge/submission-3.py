class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        #someone who's outdegree is 0
        #someone who's indegree is n-1

        outDegree = {}
        inDegree = {}

        for p1,p2 in trust:
            if p1 not in inDegree:
                inDegree[p1] = 0
                outDegree[p1] = 0
            
            if p2 not in inDegree:
                inDegree[p2] = 0
                outDegree[p2] = 0
            
            outDegree[p1]+=1
            inDegree[p2]+=1
        
        for key in outDegree:
            if outDegree[key] == 0 and inDegree[key] == n-1:
                return key
        
        return -1


