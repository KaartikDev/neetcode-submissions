class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #take adj mat --> adj list

        #do bfs on adj list and count components

        
        adjMap = {}
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i not in adjMap:
                    adjMap[i] = []
                if j not in adjMap:
                    adjMap[j] = []

                if i == j: #going to ignore self edges
                    continue
                if isConnected[i][j] == 1:
                    adjMap[i].append(j) #we only do i->j edge as this loop processes entire matrix, even j->i paring
            
        print(adjMap)
        visited = set()
        def bfs(start):
            queue = deque([start])
            while queue:
                curr = queue.popleft()
                for nei in adjMap[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        provs = 0
        for city in range(n):
            if city not in visited:
                provs+=1
                bfs(city)
        return provs

