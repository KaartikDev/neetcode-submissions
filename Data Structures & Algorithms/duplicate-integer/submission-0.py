class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempSet = set(nums)
        print(tempSet)
        return len(tempSet) != len(nums) #Do not equal as duplicates will change length