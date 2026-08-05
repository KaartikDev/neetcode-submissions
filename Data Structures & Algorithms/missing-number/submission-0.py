class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = n*(n+1)/2
        realSum = sum(nums)

        diff = int(expectedSum - realSum)
        # print(expectedSum,realSum,diff)

        return diff