class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        indegree = {}
        outdegree = {}
        for a,b in trust:
            indegree[b] = indegree.get(b,0)+1
            outdegree[a] = outdegree.get(a,0)+1
        
        print(indegree,outdegree)
        for node in indegree:
            #len outdegree us totoal number of nodes pointing to judge
            if indegree[node] == len(outdegree) and node not in outdegree:
                return node
        return -1