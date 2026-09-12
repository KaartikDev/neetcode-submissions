class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groundVal = ord('a')

        #same freq map go together
        
        
        freqToWordMap = {}
        for word in strs:
            freqCount = [0] * 26
            for c in word:
                freqCount[ord(c)-groundVal]+=1
            
            castedFreq = tuple(freqCount)
            if castedFreq not in freqToWordMap:
                freqToWordMap[castedFreq] = []
            
            freqToWordMap[castedFreq].append(word)
        
        # print(freqToWordMap)
        res = []
        for key in freqToWordMap:
            currFreqWords = []
            for word in freqToWordMap[key]:
                currFreqWords.append(word)
            res.append(currFreqWords)
        # print(res)
        return res

                