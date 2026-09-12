class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = 1
        activeChars = set([s[l]])
        best = 0
        while r < len(s):
            while s[r] in activeChars:
                activeChars.remove(s[l])
                l+=1
            activeChars.add(s[r])
            r+=1
            best = max(best,r-l)
        return best

            