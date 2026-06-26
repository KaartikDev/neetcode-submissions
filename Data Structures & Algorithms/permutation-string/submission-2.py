class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): #cant have s1 be bigger than s2
            return False
    
        abc = "abcdefghijklmnopqrstuvwxyz"
        freqMap = {} #initilize empty freq map for lower case letters
        for c in abc:
            freqMap[c] = 0
        
        #Build a check frequency map for s1
        checkMap = {}
        for c in s1:
            if c not in checkMap:
                checkMap[c] = 1
            else:
                checkMap[c] += 1
        
        l = 0
        r = 0

        while r < len(s1): #build first subtring
            freqMap[s2[r]] += 1
            r+=1
        
        r-=1
        # print(s2[l:r+1], l ,r)

        while r < len(s2):
            done = True
            for key in checkMap: #at most check map is 26 long so this is O(26) --> O(1) time complexity
                if checkMap[key] != freqMap[key]:
                    done = False
            
            if done:
                # print(s2[l:r+1], l ,r)
                return True
            
            freqMap[s2[l]] -= 1
            l+=1
            r+=1
            if r < len(s2):
                freqMap[s2[r]] += 1

        return False



        

        