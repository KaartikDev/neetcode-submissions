class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2: #empty or single char gaurd
            return len(s)

        
        l = 0
        r = 0
        freqMap = {}
        maxFoundFreq = 0
        maxFoundLen = 0
        while r < len(s):
            if s[r] not in freqMap:
                freqMap[s[r]] = 1
            else:
                freqMap[s[r]] += 1
            
            maxFoundFreq = max(maxFoundFreq,freqMap[s[r]])
            while r-l+1 - maxFoundFreq > k:
                freqMap[s[l]] -= 1
                l+=1
            
            maxFoundLen = max(r-l+1,maxFoundLen)
            r+=1
        
        return maxFoundLen


