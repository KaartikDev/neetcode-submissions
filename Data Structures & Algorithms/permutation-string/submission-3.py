class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #trivial cases
        if len(s2) < len(s1):
            return False
        elif s1 == s2:
            return True
        
        windowFreqCount = [0]*26
        s1FreqCount = [0]*26

        for i in range(len(s1)):
            s1FreqCount[ord(s1[i])-ord('a')]+=1
            windowFreqCount[ord(s2[i])-ord('a')] += 1 
        
        l = 0
        r = len(s1)-1
        
        while r<len(s2):
            # print(s1FreqCount,windowFreqCount)
            if s1FreqCount == windowFreqCount:
                return True
            windowFreqCount[ord(s2[l])-ord('a')]-=1
            l+=1
            r+=1
            if r < len(s2):
                windowFreqCount[ord(s2[r])-ord('a')]+=1
        return  s1FreqCount == windowFreqCount
        