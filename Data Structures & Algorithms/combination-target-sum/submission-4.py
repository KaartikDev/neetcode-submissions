class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        unorderedCombos = []

        currCombo = []

        def dfs(netRemainder):
            if netRemainder == 0:
                # print("found!")
                unorderedCombos.append(currCombo.copy())
                return None
            if netRemainder < 0:
                return None
            
            for v in nums:
                currCombo.append(v)
                # print(currCombo,netRemainder,v)
                dfs(netRemainder-v)
                currCombo.pop()
        
        dfs(target)

        #now all i need to do is remove duplicates....sort each list, convert to tuple, add to set, convert back to list
        resSet = set()
        for combo in unorderedCombos:
            sortedTuple = tuple(sorted(combo))
            resSet.add(tuple(sorted(combo)))
        finalRes = []
        for combo in resSet:
            finalRes.append(list(combo))
        print(len(unorderedCombos))
        return finalRes

        #so recrursive depth is O(target//min(nums)+1)...is this len(nums)^n*n time complexity?




