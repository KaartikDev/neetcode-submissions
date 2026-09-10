class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = [[] for _ in range(n)]
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        print(adjList)

        seen = set()
        def bfs(start):
            # print("bfs start = ", start)
            queue = deque([start])
            while queue:
                curr = queue.popleft()
                # print("bfs curr is=",curr)
                for nei in adjList[curr]:
                    # print("layer nei=",nei)
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
        
        count = 0
        for i in range(n):
            if i not in seen:
                count+=1
                seen.add(i)
                bfs(i)
        return count


