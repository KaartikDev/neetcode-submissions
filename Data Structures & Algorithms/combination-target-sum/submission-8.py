class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        unorderedCombos = []

        currComboMap = {}
        for v in nums:
            currComboMap[v] = 0
        
        seenCombos = set()

        def dfs(netRemainder):
            if netRemainder == 0:
                # print("found!")
                currComboList = []
                for v in nums:
                    for i in range(currComboMap[v]):
                        currComboList.append(v)
                unorderedCombos.append(currComboList)
                return None
            if netRemainder < 0:
                return None
            
            for v in nums:
                currComboMap[v]+=1
                
                currComboList = []
                for n in nums:
                    for i in range(currComboMap[n]):
                        currComboList.append(n)
                currComboTuple = tuple(currComboList)

                if currComboTuple not in seenCombos:
                    seenCombos.add(currComboTuple)
                    dfs(netRemainder-v)
                # print(currCombo,netRemainder,v)
                currComboMap[v]-=1
        
        dfs(target)

        #now all i need to do is remove duplicates....sort each list, convert to tuple, add to set, convert back to list
        resSet = set()
        for combo in unorderedCombos:
            sortedTuple = tuple(sorted(combo))
            resSet.add(tuple(sorted(combo)))
        finalRes = []
        for combo in resSet:
            finalRes.append(list(combo))
        # print(len(unorderedCombos),len(finalRes)) --> we are doing crap ton of extra work.
        return finalRes

        #so recrursive depth is O(target//min(nums)+1)...is this len(nums)^n*n time complexity?




