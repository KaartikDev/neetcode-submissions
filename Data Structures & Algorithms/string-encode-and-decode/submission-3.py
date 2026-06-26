class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "EMPTY LIST INPUT"
        
        #Idea do a repeated charcter compression with 2 pointers and then use '###' as break between words
        finStr = ""
        wordBreak = "###"
        emptyStringHolder = '@'
        for word in strs:
            currChar = ''
        
            if len(word) > 0: #epmty word gaurd
                currChar = word[0]
            else:
                finStr += emptyStringHolder
                finStr += wordBreak
                continue
            
            letterP = 0
            letterCount = 0


            while letterP < len(word):
                if word[letterP] == currChar:
                    letterCount+=1 #increase the number of times this char appears consecutivles
                    letterP+=1 #move down the owrd
                else:
                    finStr += currChar + str(letterCount) #append the letter and num times it appeared consecutivles
                    letterCount = 0
                    currChar = word[letterP] #update the current character
            
            finStr += currChar + str(letterCount) #append the last letter and its count
            finStr += wordBreak
        print(finStr)
        return finStr
            



    def decode(self, s: str) -> List[str]:
        if s == "EMPTY LIST INPUT":
            return []
        
        strList = s.split("###")
        for i,word in enumerate(strList):
            recoverWord = ""
            if word == '@': #remeber the empty string gaurd
                strList[i] = recoverWord 
                continue
            currCharP = 0
            while currCharP < len(word):
                recoverWord += word[currCharP] * int(word[currCharP+1]) #multiply by the char by num times it appeared
                currCharP+=2 #increase by 2 as every other letter is the character to reproduce
            strList[i] = recoverWord
        
        
        return strList[:len(strList)-1] #need to trim off the extra empty stirng split makes at the end
