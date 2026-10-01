class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #some form of sliding window


        charCounts = [0] * 26
        r = 0
        l = 0

        best = 0

        while r < len(s):
            charCounts[ord("A")-ord(s[r])]+=1
            while sum(charCounts)-max(charCounts) > k:
                charCounts[ord("A")-ord(s[l])]-=1
                l+=1
            best = max(best,sum(charCounts))
            r+=1

        return best
