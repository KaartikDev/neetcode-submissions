class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        checkMap = {} #unique chacracters
        for c in t:
            if c not in checkMap:
                checkMap[c] = 1
            else:
                checkMap[c] += 1
        print(checkMap)
        #brute force solution check a window staring from len(checkMap) up to len(s)
        k = len(checkMap)
        r = 0
        while k-1 < len(s):
            r = 0

            while r + k -1 < len(s):
                currWindow = s[r:r+k]

                tempMap = {}
                for c in currWindow:
                    if c not in tempMap:
                        tempMap[c] = 1
                    else:
                        tempMap[c] += 1
                
                if len(currWindow) > 5:
                    print(tempMap)

                done = True
                for key in checkMap:
                    if key not in tempMap or tempMap[key] < checkMap[key]:
                        done = False
                        break
                
                if done:
                    return currWindow      
                       
                r+=1
            k+=1
        
        return ""
