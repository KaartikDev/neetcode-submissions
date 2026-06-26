class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): #diff length strenghst cant work
            return False
        
        freqMap1 = {}
        freqMap2 = {}

        for i in range(len(s)): #both str have same length
            s_char = s[i] 
            t_char = t[i]

            #create frequecy maps
            if s_char not in freqMap1: 
                freqMap1[s_char] = 1
            else:
                freqMap1[s_char] += 1
            
            if t_char not in freqMap2:
                freqMap2[t_char] = 1
            else:
                freqMap2[t_char] += 1
        
        for s_char in freqMap1:
            if s_char not in freqMap2 or freqMap1[s_char] != freqMap2[s_char]: #If a character does not exist OR frequency count for charcters do not match
                return False

        return True #passes all checks

            

        