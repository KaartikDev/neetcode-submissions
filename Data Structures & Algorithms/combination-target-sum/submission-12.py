class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []
        def dfs(i,netRemainder):
            if i >= len(nums):
                if netRemainder == 0:
                    res.append(curr.copy())
                return
            
            if netRemainder - nums[i] >= 0:
                curr.append(nums[i])
                dfs(i,netRemainder-nums[i])
                curr.pop()
            dfs(i+1,netRemainder)
        dfs(0,target)
        return res
            





