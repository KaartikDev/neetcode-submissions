class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #use a dict and while count of char is not zero scanning left to right u need to keep going
        #we need to ensure count of ALL chars in window are zero
        freqMap = {}
        for c in s:
            freqMap[c] = freqMap.get(c,0)+1
        

        l,r = 0,0
        activeChars = set()
        
        res = []
        #scan left to right 
        # adding chars to active until every char in our substr window has zero freq 
        # now we partion and update bounds
        while r < len(s):
            # print("entry l,r=",l,r,activeChars,freqMap)
            activeChars.add(s[r]) # add curr to unqiue chars in subtring

            freqMap[s[r]]-=1 #decrease freq because one more char accounted for

            if freqMap[s[r]] == 0: #if no more chars remain in we can remove it from active chars
                activeChars.remove(s[r]) #aka cant appear in future
           
            if len(activeChars) == 0: #if no more active chars we can partion here
                res.append(r-l+1)
                l = r+1
            r+=1

        
        
        return res
                
            