class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1: #empty/single char only gaurd
            return len(s)
        

        freqMap = {}
        maxFreq = 0
        maxLenFound = 0

        l = 0
        

        for r in range(len(s)):

            if s[r] not in freqMap:
                freqMap[s[r]] = 1
            else:
                freqMap[s[r]] += 1
            
            maxFreq = max(maxFreq,freqMap[s[r]])

            #Valid when (len sub str) - maxFreq <= k
            #Invalid when not above
            # print(r,l,maxFreq)
            while (r-l+1) - maxFreq > k:
                # print(l)
                freqMap[s[l]] -= 1
                l+=1
            
            # print(s[l:r+1], l, r)
            maxLenFound = max(maxLenFound,r-l+1)

        return maxLenFound