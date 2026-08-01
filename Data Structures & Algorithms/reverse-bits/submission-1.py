class Solution:
    def reverseBits(self, n: int) -> int:
        #okay

        binaryRep = []
        temp = n
        for i in range(32):
            binaryRep.append(str(temp&1))
            temp>>=1
        # print(binaryRep)
        return int("".join(binaryRep),2)