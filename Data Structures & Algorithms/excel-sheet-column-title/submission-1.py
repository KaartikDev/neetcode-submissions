class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #letter map
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letMap = {}
        i = 0
        for c in letters:
            letMap[i] = c
            i+=1
        
        res = ""
        while columnNumber > 0:
            columnNumber-=1 # we do to go to zero indexing
            mod = (columnNumber) % 26
            

            res+=letMap[mod]

            columnNumber//=26
        return res[::-1]

