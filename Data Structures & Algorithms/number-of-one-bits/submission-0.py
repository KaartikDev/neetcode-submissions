class Solution:
    def hammingWeight(self, n: int) -> int:
        #counting the number of ones??
        # << >> ~ ^ & |
        # print(n)

        base = 0b1
        count = 0
        for i in range(32):
            if base & n:
                count+=1
            n>>=1

        return count