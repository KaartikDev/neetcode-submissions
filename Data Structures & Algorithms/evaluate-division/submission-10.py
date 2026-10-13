class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # Want variable --> value



        #if a path exists from either a to b or b to a we win?

        #say we want A/C
        #we have A/B and B/C

        #so then starting from A we want to get to C, multiplying as we go

        #so we build an adj map treating eqations as edges
        #we create a value map?

        #NOTE: We also have all B/A edges just need to store 1/Value
        adjMap = {}
        valMap = {}
        i = 0
        while i < len(equations):
            a,b = equations[i]
            val = values[i]
            if a not in adjMap:
                adjMap[a] = []
            if b not in adjMap:
                adjMap[b] = []
            
            adjMap[a].append(b)
            adjMap[b].append(a)
            valMap[(a,b)] = val
            valMap[(b,a)] = 1/val
            # valMap[(a,a)] = 1
            # valMap[(b,b)] = 1
            i+=1
        
        def dfs(curr,end,visited):
            if curr == end:
                return 1.0
            
            visited.add(curr)
            for nei in adjMap.get(curr,[]):
                if nei not in visited:
                    remainingProd = dfs(nei,end,visited)
                    if remainingProd != -1:
                        return remainingProd * valMap[(curr,nei)]
            return -1
        
        
        res = []
        for q1,q2 in queries:
            if q1 not in adjMap or q2 not in adjMap:
                res.append(-1)
            else:
                res.append(dfs(q1,q2,set()))
        return res
    
            










