class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderMap = {}
        for i,c in enumerate(order):
            orderMap[c] = i
        # print(orderMap)

        for i in range(len(words)-1):
            firstWord = words[i]
            secondWord = words[i+1]

            #check secondWord is not prefix of firstWord
            if firstWord.startswith(secondWord):
                print(firstWord,secondWord)
                return False
            
            
            # if isPrefix: #if prefix second, we out of order
            #     return False
            
            #now to check the ordering
            i = 0
            while i < len(firstWord) and i < len(secondWord):
                if orderMap[secondWord[i]] < orderMap[firstWord[i]]:
                    return False
                elif orderMap[secondWord[i]] > orderMap[firstWord[i]]:
                    break #found letter which is greater
                else: #do nothing if equal letters
                    pass
                i+=1
        
        return True
                    
                
