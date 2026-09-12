class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #some form of sliding window

        if len(s) <= 1:
            return len(s)
        

        alphaCount = [0] * 26
        #currLen-max(Acount) <= k and we happy
        l = 0
        r = 0

        res = 0
        while r < len(s):
            # add new character
            alphaCount[ord("A")-ord(s[r])]+=1
            r+=1
            
            #shrink while num swaps > k
            while (r-l)-max(alphaCount) >  k:
                alphaCount[ord("A")-ord(s[l])]-=1
                l+=1
            
            
            #update res
            res = max(res,r-l)
            
        return res
    
            







