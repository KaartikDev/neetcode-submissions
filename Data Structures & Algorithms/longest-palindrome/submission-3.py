class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqMap = {}
        for c in s:
            freqMap[c] = freqMap.get(c,0)+1
        
        #check if atleast one char has odd freq of one
        oneOdd = False
        
        res = 0

        #key idea: palindorm has one odd count char and otherwise all even
        for c in freqMap:

            if freqMap[c] % 2 == 1: #save the odd count for later
                oneOdd=True

                res+=max(0,freqMap[c]-1)
            else:
                res+=freqMap[c]
            
        print(freqMap)
        
        #take the one odd count char as center add include all even counts
        if oneOdd:
            return res+1
        else: #res gaurnteed to be made of even count chars and be even
            return res
        
            
