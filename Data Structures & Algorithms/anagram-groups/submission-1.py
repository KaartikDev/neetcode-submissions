import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Ideal sol
        charFreqToWordsHash = {}

        for currStr in strs:
            count = [0] * 26 #creating an empty frequency count

            for c in currStr: #count the number of characters in each word
            #ord(c) --> oridnal of c gives unicode
                count[ord(c)-ord('a')] += 1 #maps chacrters to 0-25 as chacrters are gaurnteed to be lowercase english chars
            
            hashableCount = tuple(count)
            if hashableCount not in charFreqToWordsHash:
                charFreqToWordsHash[hashableCount] = [currStr]
            else:
                charFreqToWordsHash[hashableCount].append(currStr)
        
        ans = []
        for key in charFreqToWordsHash:
            ans.append(charFreqToWordsHash[key])
        return ans 


        # copyList = strs.copy()
        # ansList = []
        # k = 0

        # while copyList:
        #     checkWord = copyList.pop()
        #     ansList.append([checkWord])
            
        #     freqMap = {}
        #     for c in checkWord:
        #         if c not in freqMap:
        #             freqMap[c] = 1
        #         else:
        #             freqMap[c] +=1
            
        #     i = 0
        #     while i < len(copyList):
        #         skipWord = False
        #         word = copyList[i]
        #         if len(word) != len(checkWord):
        #             skipWord = True
                
        #         currFreqMap = {}
        #         for c in word:
        #             if c not in currFreqMap:
        #                 currFreqMap[c] = 1
        #             else:
        #                 currFreqMap[c] += 1
                
        #         for c in checkWord:
        #             if c not in currFreqMap or freqMap[c] != currFreqMap[c]:
        #                 skipWord = True
                
        #         if not skipWord:
        #             ansList[k].append(word)
        #             copyList.pop(i)
        #         else:
        #             i+=1

        #     k+=1

        # return ansList
        # # O(N^2*L) --> N is num words and L is longest word length
        # # O(N*L) space complexity --> make n freq maps with L being longets length


            
