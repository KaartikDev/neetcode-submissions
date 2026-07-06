class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #is this some sort of topoloigical orering?
        # a topological ordering means an ordering of all nodes in a graph so that u never run into depednancy issues 
        # use kahns algo for topological ordering check
        
        #We need to do this on charcter level
        #IDEA: look at when two words differ (then u get charcter a < b) by comapring word indices

        alpha = set("".join(words))
        dependancyGraph = {}
        indegreeMap = {}
        for c in alpha:
            dependancyGraph[c] = set()
            indegreeMap[c] = 0

        
        
        def nextDiffChars(str_a,str_b):
            a_pointer = 0
            b_pointer = 0
            while a_pointer < len(str_a) and b_pointer < len(str_b) and str_a[a_pointer] == str_b[b_pointer]:
                a_pointer+=1
                b_pointer+=1
                
            if a_pointer < len(str_a) and b_pointer < len(str_b):
                return (str_a[a_pointer], str_b[b_pointer])
            else:
                return None
        
        for i in range(len(words)-1):
            str_a, str_b = words[i], words[i+1]
            if len(str_a) > len(str_b) and str_a.startswith(str_b):
                return ""
            
            diff = nextDiffChars(str_a, str_b)
            if diff:
                u, v = diff
                if v not in dependancyGraph[u]:
                    dependancyGraph[u].add(v)
                    indegreeMap[v] += 1

        # print(dependancyGraph)
        # print(indegreeMap)



        #now we need to do khans algo
        queue = deque()
        for c in indegreeMap:
            if indegreeMap[c] == 0:
                queue.append(c)
        
        res = []

        while queue:
            availableLetter = queue.popleft()
            res.append(availableLetter)

            for dependantLetter in dependancyGraph[availableLetter]:
                indegreeMap[dependantLetter]-=1
                if indegreeMap[dependantLetter] == 0:
                    queue.append(dependantLetter)
        
        # print(res)

        if len(res) == len(alpha):
            return "".join(res)
        else:
            return ""


                
                


        
        
        
        
        
        #WRONG APPROACH!!!! 
        # build an adjMap with u -> v meaning u is prefix of v.
        # Run kahns algo, whne u process a node add all remaining suffix charcters. 
        # if u ever add a non-unique charcter or nodes left not possible

        
        
        # def buildAdjMap(words):
        #     adjMap = {}
        #     for str_a in words:
        #         adjMap[str_a] = []
        #         for str_b in words:
        #             if str_a == str_b:
        #                 continue
        #             if str_b.startswith(str_a):
        #                 adjMap[str_a].append(str_b)
        #     print(adjMap)

        #     return adjMap
        
        # adjMap = buildAdjMap(words)


