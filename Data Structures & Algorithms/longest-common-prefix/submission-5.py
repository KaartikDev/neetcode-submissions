class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0
        r = 0

        while r < len(strs[0]):
            curr = strs[0][r]
            isGood = True
            for word in strs:
                if r >= len(word) or curr != word[r]:
                    isGood = False
                    break
            
            if isGood:
                r+=1
            else:
                break
        
        return strs[0][l:r]
