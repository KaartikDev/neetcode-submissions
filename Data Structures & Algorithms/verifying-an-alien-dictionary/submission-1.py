class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = i
        
        for i in range(len(words)-1):
            str_a = words[i]
            str_b = words[i+1]

            #cant have prefix come second in odered list
            if str_a.startswith(str_b):
                return False
            
            j = 0
            while j < len(str_a):
                #check first diff chars correct order
                if str_a[j] != str_b[j]: 
                    if orderMap[str_a[j]] > orderMap[str_b[j]]:
                        return False
                    else: #confirmed str a before str b, stop checking now
                        break
                j+=1
            
        return True
