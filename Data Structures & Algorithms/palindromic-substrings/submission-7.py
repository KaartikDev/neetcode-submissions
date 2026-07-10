class Solution:
    def countSubstrings(self, s: str) -> int:
        #top down recrusive strategy 
        # dp(l,r) is palindrome if dp(l+1,r-1) is palindrome and and s[l] == s[r-1] 

        if len(s) <= 1:
            return len(s)
        table = [[None]*(len(s)+1) for _ in range(len(s)+1)]

        
        def dp(l,r):
            #l is inclusive
            #r is exlcusive
            # if l < 0 or r < 0 or l >= len(s) or r > len(s)+1:
            #     return False
            
            if r - l <= 1:
                return True
            if table[l][r]:
                return table[l][r]
            
            table[l][r] = s[l] == s[r-1] and dp(l+1,r-1)
            return table[l][r]
        
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if dp(i,j):
                    count+=1
        
        # print(table)
        return count
            
        
        
        
        
        #brute force 
        #make set of all substr --> O(n^2) subtrings each O(n) long
        #check isPalin on all O(n^2) subtrings --> O(n^3) time, O(n^3) space 
