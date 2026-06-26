class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMapS = {}
        freqMapT = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in freqMapS:
                freqMapS[s[i]] = 1
            else:
                freqMapS[s[i]]+=1
            
            if t[i] not in freqMapT:
                freqMapT[t[i]] = 1
            else:
                freqMapT[t[i]]+=1
        
        return freqMapT == freqMapS


        