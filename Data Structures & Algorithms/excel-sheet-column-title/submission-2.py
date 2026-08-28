class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #letter map
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letMap = {}
        i = 1
        for c in letters:
            letMap[i] = c
            i+=1
        
        res = ""
        while columnNumber > 0:
            mod = columnNumber % 26
            
            if mod == 0:
                mod = 26
                columnNumber-=1

            res+=letMap[mod]

            columnNumber//=26
        return res[::-1]

