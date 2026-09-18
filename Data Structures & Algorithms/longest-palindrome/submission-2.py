class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqMap = {}
        for c in s:
            freqMap[c] = freqMap.get(c,0)+1
        
        #check if atleast one char has odd freq of one
        oneOdd = False
        
        #take even count chars and place on ends of str
        res = 0
        for c in freqMap:
            if freqMap[c] % 2 == 1:
                oneOdd=True

                res+=max(0,freqMap[c]-1)
            else:
                res+=freqMap[c]
            
        print(freqMap)
        
        #take the one odd count char as center add include all even counts
        if oneOdd:
            return res+1
        else: #alr all even counts res
            return res
        
            
