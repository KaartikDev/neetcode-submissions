class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allSeen = set()
        finCompliment = 0
        finI = 0
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in allSeen:
                finCompliment = compliment
                finI = i
            else:
                allSeen.add(nums[i])
        
        for j in range(len(nums)):
            if nums[j] == finCompliment and finI != j:
                ans = [finI,j]
                ans.sort()
                return ans
            
        return [0,0]
        