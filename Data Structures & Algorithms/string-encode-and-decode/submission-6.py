class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            for c in word:
                s+=str(ord(c))
                s+=":" #new char
            s+="." #new word
        s+='#' #end string
        print(s)
        return s
        


    def decode(self, s: str) -> List[str]:
        
        if s == "#":
            return []
        if s == ".#":
            return [""]
        
        ans = []
        i = 0
        
        while i < len(s) and s[i] != '#':
            currWord = ""
            while i < len(s) and s[i] != ".":
                temp = ""
                while i < len(s) and s[i] != ':':
                    temp+=s[i]
                    i+=1
                try:
                    currWord+=chr(int(temp))
                except:
                    print(temp)
                i+=1
            ans.append(currWord)
            i+=1
        print(ans)
            
        return ans
