class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        
        for currNum in range(n+1):
            count = 0
            leftOver = currNum
            for i in range(10): #by contraints max n is 1000, 2^10>1000
                if leftOver & 1:
                    count+=1
                leftOver>>=1
            res.append(count)
        return res