import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copyList = strs.copy()
        ansList = []
        k = 0

        while copyList:
            checkWord = copyList.pop()
            ansList.append([checkWord])
            
            freqMap = {}
            for c in checkWord:
                if c not in freqMap:
                    freqMap[c] = 1
                else:
                    freqMap[c] +=1
            
            i = 0
            while i < len(copyList):
                skipWord = False
                word = copyList[i]
                if len(word) != len(checkWord):
                    skipWord = True
                
                currFreqMap = {}
                for c in word:
                    if c not in currFreqMap:
                        currFreqMap[c] = 1
                    else:
                        currFreqMap[c] += 1
                
                for c in checkWord:
                    if c not in currFreqMap or freqMap[c] != currFreqMap[c]:
                        skipWord = True
                
                if not skipWord:
                    ansList[k].append(word)
                    copyList.pop(i)
                else:
                    i+=1

            k+=1

        return ansList


            
