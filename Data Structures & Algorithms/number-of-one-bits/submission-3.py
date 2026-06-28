class Solution:
    def hammingWeight(self, n: int) -> int:
        #counting the number of ones??
        # << >> ~ ^ & |
        # print(n)

        
        count = 0
        for i in range(32):
            if n & 1:
                count+=1
            n>>=1

        return count