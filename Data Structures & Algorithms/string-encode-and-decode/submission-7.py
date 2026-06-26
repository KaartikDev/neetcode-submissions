class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += str(len(word)) + "#" + word
        
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        ans = []
        if s == "":
            return []
        
        i = 0
        while i < len(s):
            currLen = ""
            while i < len(s) and s[i] != '#':
                currLen+=s[i]
                i+=1
            
            i+=1 #get off hashtag char
            ans.append(s[i:i+int(currLen)]) #slice correct val

            i+=int(currLen) #move to next valid int start
        print(ans)
        return ans


