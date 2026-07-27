class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #use a dict and while count of char is not zero scanning left to right u need to keep going
        #we need to ensure count of ALL chars in window are zero
        freqMap = {}
        for c in s:
            freqMap[c] = freqMap.get(c,0)+1
        

        l,r = 0,0
        windowChars = set()
        
        partionBounds = []
        while l < len(s) and r < len(s):
            # print("entry l,r=",l,r,windowChars,freqMap)
            windowChars.add(s[r])

            freqMap[s[r]]-=1

            if freqMap[s[r]] == 0:
                windowChars.remove(s[r])
           
            if len(windowChars) == 0:
                partionBounds.append((l,r))
                l = r+1
            r+=1
        print(partionBounds)
        res = []
        for part in partionBounds:
            l = part[0]
            r = part[1]
            if l == r:
                res.append(1)
            else:
                res.append(r-l+1)



        #time to process res, its r-l+1 for len and if l == r then ret 1

        return res
                
            