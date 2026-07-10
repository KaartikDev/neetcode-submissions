class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalin(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        #one sol: build all possible substrings
        #check for longest one
        subStrSet = set()
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                   subStrSet.add(s[i:j])
        # print(subStrSet)   

        best = ""
        for curr in subStrSet:
            if isPalin(curr) and len(curr) > len(best):
                best = curr
        return best