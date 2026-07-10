class Solution:
    def longestPalindrome(self, s: str) -> str:
        #we add both sides or not, we start at middle
        if len(s) <= 1:
            return s
        
        #O(n^2) time
        #O(1) space
        best = (0,1) #l,r
        for i in range(len(s)):
            
            #odd len palindromes
            l = i-1
            r = i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            if r - l - 1 > best[1] - best[0]:
                best = (l+1,r) #for last valid palin need to correct by moving l (inclusive), r (exlcusive)
            
            #even len palidnroms
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            if r - l - 1 > best[1] - best[0]:
                best = (l+1,r)
        
        return s[best[0]:best[1]]



        # #brute force method O(n^3) time, O(n^2) space
        # def isPalin(s):
        #     l = 0
        #     r = len(s)-1
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l+=1
        #         r-=1
        #     return True

        # #one sol: build all possible substrings
        # #check for longest one
        # subStrSet = set()
        # for i in range(len(s)):
        #     for j in range(i,len(s)+1):
        #            subStrSet.add(s[i:j])
        # # print(subStrSet)   

        # best = ""
        # for curr in subStrSet:
        #     if isPalin(curr) and len(curr) > len(best):
        #         best = curr
        # return best