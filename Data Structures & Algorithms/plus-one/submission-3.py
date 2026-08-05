class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringDigits = [str(d) for d in digits]
        plusOne = int("".join(stringDigits)) + 1

        return list(str(plusOne))
