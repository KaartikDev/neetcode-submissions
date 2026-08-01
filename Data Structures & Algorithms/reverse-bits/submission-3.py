class Solution:
    def reverseBits(self, n: int) -> int:

        reverseBinaryRep = []
        temp = n
        for i in range(32):
            reverseBinaryRep.append(str(temp&1))
            temp>>=1
        
        
        binaryStr = ("".join(reverseBinaryRep))
        res = 0
        for p in range(len(binaryStr)):
            index = len(binaryStr)-p-1
            res+=(int(binaryStr[index])* (2**p))
        
        return res