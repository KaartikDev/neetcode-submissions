class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # all 0 if two identical number zero'd
        base = 0b0
        for num in nums:
            base^=num
        return base
