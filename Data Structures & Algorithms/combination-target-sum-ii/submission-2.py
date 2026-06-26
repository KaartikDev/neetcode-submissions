class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        currCandidates = []

        def dfs(i,netRemainder):
            if netRemainder == 0:
                # print('found!',netRemainder,currCandidates)
                res.append(currCandidates.copy())
                return None
            if netRemainder < 0 or i >= len(candidates):
                # print("rejected!",currCandidates)
                return None
            
            
            currCandidates.append(candidates[i])
            count = 0
            # print(currCandidates)
            dfs(i+1,netRemainder-candidates[i])
            while i < len(candidates)-1 and candidates[i+1]==candidates[i]:
                i+=1
            currCandidates.pop()
            dfs(i+1,netRemainder)
            # dfs(currCandidates,netRemainder)
        
        dfs(0,target)
        return res
