class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        for el in nums:
            res.append(el)
        return res