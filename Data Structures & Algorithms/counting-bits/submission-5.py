class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
            
        res = []
        MAX_SHIFTS = math.ceil(math.log2(n)) + 1
        
        for currNum in range(n+1):
            count = 0
            leftOver = currNum
            for i in range(MAX_SHIFTS): 
                if leftOver & 1:
                    count+=1
                leftOver>>=1
            res.append(count)
        return res
        #time O(n) space O(n)