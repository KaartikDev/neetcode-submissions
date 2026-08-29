class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = i
        
        for i in range(len(words)-1):
            str_a = words[i]
            str_b = words[i+1]

            if str_a.startswith(str_b):
                return False
            
            for j in range(len(str_a)):
                if str_a[j] != str_b[j]:
                    if orderMap[str_a[j]] > orderMap[str_b[j]]:
                        return False
                    else:
                        break
            
        return True
