class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groundVal = ord('a')

        groupHash = {}

        for word in strs:
            temp = [0] * 26
            for c in word:
                temp[ord(c) - groundVal] += 1
            currFreq = tuple(temp)

            if currFreq not in groupHash:
                groupHash[currFreq] = [word]
            else:
                groupHash[currFreq].append(word)
        
        ans = []
        for key in groupHash:
            ans.append(groupHash[key])
        
        return ans
        
        # groundVal = ord('a')
        # wordMap = {}
        # for i in range(len(strs)):
        #     charMapArr = [0] * 26
        #     # print(temp)

        #     for c in strs[i]:
        #         alphEnc = ord(c) - groundVal
        #         charMapArr[alphEnc]+=1
        #     charMapTuple = tuple(charMapArr)
            
        #     if charMapTuple not in wordMap:
        #         wordMap[charMapTuple] = [strs[i]]
        #     else:
        #         wordMap[charMapTuple].append(strs[i])
                
        # return list(wordMap.values())
            
