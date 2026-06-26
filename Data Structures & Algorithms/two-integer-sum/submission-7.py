class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allSeen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in allSeen:
                smaller = min(i,allSeen[compliment])
                bigger = max(i,allSeen[compliment])
                return [smaller,bigger]
            else:
                allSeen[nums[i]] = i
            
        return [-1,-1] # incorrect input gaurd