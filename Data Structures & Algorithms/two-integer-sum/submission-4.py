class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #intend sol with hash map

        indexHash = {}

        for i in range(len(nums)):
            curr = nums[i]

            complement = target - curr 

            if complement in indexHash: #see if we have found complment before
                big_ind = max(i,indexHash[complement])
                small_ind = min(i,indexHash[complement])
                return [small_ind, big_ind]

            if nums[i] not in indexHash:
                indexHash[nums[i]] = i
            
                
        