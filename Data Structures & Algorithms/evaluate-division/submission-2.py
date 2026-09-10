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
            i+=1
        
        def findPath(start,end):
            path = []
            visited = set()
            def dfs(curr,end):
                path.append(curr)
                visited.add(curr)

                if curr == end and curr in adjMap:
                    return path
                
                for nei in adjMap.get(curr,[]):
                    if nei not in visited:
                        res = dfs(nei,end)
                        if res:
                            return res
                path.pop()
                return None
            
            return dfs(start,end)

                    

        # print(adjMap)
        # print(valMap)
        # print(findPath("a","c"))
        j = 0
        res = []
        while j < len(queries):
            f,g = queries[j]
            path = findPath(f,g)
            print(path)

            if not path or len(path) == 0:
                res.append(-1)
            elif len(path) == 1:
                res.append(1)
            else:
                #traverse path, multiplying as we go
                running = valMap[(path[0],path[1])]
                
                for q in range(1,len(path)-1):
                    running*=valMap[(path[q],path[q+1])]
                print(running)

                res.append(running)
            
            j+=1
        return res

        res = 1










