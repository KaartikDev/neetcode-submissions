class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
                return s
        
        def isPalin(s):
            l = 0
            r = len(s)-1

            
            
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        best = ""
        l = 0
        r = 1

        #one sol: build all possible substrings
        #check for longest one
        subStrSet = set()
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                   subStrSet.add(s[i:j])
        # print(subStrSet)   

        best = ""
        for s in subStrSet:
            if isPalin(s) and len(s) > len(best):
                best = s
        return best