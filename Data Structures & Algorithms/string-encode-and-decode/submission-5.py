class Solution:

    def encode(self, strs: List[str]) -> str:
        finStr = ""

        for word in strs:
            finStr += str(len(word)) + '#' + word
        print(finStr)
        return finStr


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        pointer = 0
        ans = []
        while pointer < len(s):
            currWordLen = ""

            while s[pointer].isnumeric():
                currWordLen+=s[pointer]
                pointer+=1
            
            currWord = s[pointer+1:pointer+1+int(currWordLen)]
            # print([s,currWord,pointer+2,pointer+2+currWordLen])
            ans.append(currWord)
            pointer+=1+int(currWordLen)
        return ans