class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()

        for i in range(len(nums)):
            mySet.add(nums[i])
        # print(mySet)
        # print(len)
        return len(mySet) != len(nums)
        