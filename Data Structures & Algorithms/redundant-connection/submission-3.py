class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    
        #v^2+ve
        #adjMap
        #degree?

        #adjMap 
        adjMap = {}
        degree = {}
        for u,v in edges:
            if u not in adjMap:
                adjMap[u] = []
                degree[u] = 0
            if v not in adjMap:
                adjMap[v] = []
                degree[v] = 0
            
            adjMap[u].append(v)
            degree[u]+=1
            adjMap[v].append(u)
            degree[v]+=1
        
        n=len(adjMap)
        st = []
        visited = set()
        for node in range(1,n+1):
            if degree[node] == 1:
                st.append(node)
                visited.add(node)
        
        #kahans alg on nodes of degree 1
        while st:
            curr = st.pop()
            for nei in adjMap[curr]:
                degree[nei]-=1
                if degree[nei] <= 1 and nei not in visited:
                    st.append(nei)
                    visited.add(nei)
        
        # print("safe=",visited)

        #now edges between unvisted nodes createt the cycle
        redunEdges = set()
        for node in range(1,n+1):
            if node not in visited:
                for nei in adjMap[node]:
                    if nei not in visited and node < nei: #make sure nei is vert in cylce and only want to add edge one wa
                        redunEdges.add((node,nei))
        
        # print("redun edges=",redunEdges)

        for i in range(len(edges)-1,-1,-1):
            if tuple(edges[i]) in redunEdges:
                return edges[i]





            