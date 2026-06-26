class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #some form of sliding window
        
        #trivial input gaurd
        if len(s) <= 1:
            return len(s)
        letterCounts = [0] * 26
        l = 0
        r = 1
        best_len = 0
        curr_skips = k
        letterCounts[ord(s[0])-ord('A')]+=1

        i = 0
        while r < len(s):
            letterCounts[ord(s[r])-ord('A')]+=1
            
            if sum(letterCounts)-max(letterCounts) <= k:
                best_len = max(best_len,r-l+1)
                r+=1
            else: #so no more changes available
                while sum(letterCounts)-max(letterCounts) > k and l < r:
                    letterCounts[ord(s[l])-ord('A')]-=1
                    l+=1
                best_len = max(best_len,r-l+1)
                r+=1
            
        
                    
        return best_len