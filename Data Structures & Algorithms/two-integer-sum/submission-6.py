class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allSeen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in allSeen:
                smallInd = min(allSeen[compliment],i)
                bigInd = max(allSeen[compliment],i)

                return [smallInd,bigInd]
            else:
                allSeen[nums[i]] = i
        
        return [-1,-1] # incorrect input gaurd