class Solution:
    def reverseBits(self, n: int) -> int:

        binaryRep = []
        temp = n
        for i in range(32):
            binaryRep.append(str(temp&1))
            temp>>=1
        # print(binaryRep)
        binaryStr = ("".join(binaryRep))
        res = 0
        for p in range(len(binaryStr)):
            index = len(binaryStr)-p-1
            res+=(int(binaryStr[index])* (2**p))
        # return int(binaryStr,2)
        return res