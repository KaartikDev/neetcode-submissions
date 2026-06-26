class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        unorderedCombos = []

        currCombo = []


        def dfs(i,netRemainder):
            if netRemainder == 0 and i < len(nums):
                unorderedCombos.append(currCombo.copy())
                return None
            if netRemainder < 0 or i >= len(nums):
                return None
            
            currCombo.append(nums[i])
            dfs(i,netRemainder-nums[i])
            # print(currCombo,netRemainder,v)
            currCombo.pop()
            dfs(i+1,netRemainder)        
        dfs(0,target)

        return unorderedCombos

        #so recrursive depth is O(target//min(nums)+1)...is this len(nums)^n*n time complexity?




