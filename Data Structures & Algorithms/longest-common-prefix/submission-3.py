class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        if not strs:
            return prefix

        for i in range(len(strs[0])):
            #check if charcter belongs for every word in list
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return prefix
            
            prefix+=strs[0][i]
        return prefix

        
        