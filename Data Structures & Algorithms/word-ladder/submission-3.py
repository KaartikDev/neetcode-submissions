class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #make a graph words are nodes and they are connected if they differ by exactly one charcter in same position
        #run bfs from start, if entire graph explored no end found return

        #can use hash map as adj list?
        #how to know if two words are one letter apart?

        #end word not in wordList gaurd:
        if endWord not in wordList:
            return 0
        #end word diff length than start (not possible with 1 letter change)
        if len(endWord) != len(beginWord):
            return 0
        
        def oneLetterApart(s1,s2): 
            if len(s1) != len(s2):
                return False
            
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff+=1
            if diff > 1:
                return False
            else:
                return True
                
        #now build an adj list
        allVertices = wordList.copy()
        allVertices.append(beginWord)
        
        def buildAdjMap(allVertices):
            adjMap = {}
            for keyWord in allVertices:
                if keyWord not in adjMap:
                    adjMap[keyWord] = []
                for neighborWord in allVertices:
                    if neighborWord == keyWord: #no self edge allowed
                        continue
                    elif oneLetterApart(keyWord,neighborWord): #valid edge
                        adjMap[keyWord].append(neighborWord)
            
            return adjMap

        adjMap = buildAdjMap(allVertices)
        print(adjMap)

        #now need to run bfs on adj map to find shortest path between two nodes as all edges same weight
        def bfs(start, end):
            pathLenght = 1
            queue = deque([start])
            visited = set([start])
            while queue:
                
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr == end:
                        return pathLenght
                    
                    for neighbor in adjMap[curr]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                pathLenght+=1
            return int(0)
        
        ans = bfs(beginWord,endWord)
        # print(ans)


        return ans




