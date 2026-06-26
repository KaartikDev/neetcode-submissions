class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #trivial case gaurds
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        if t == "":
            return t

        bestPointers = [-1,-1]
        bestLen = float('inf')

        windowFreq = {}
        t_freq = {}
        
        
        for c in t:
            t_freq[c] = t_freq.get(c,0) + 1
        
        have = 0
        need = len(t_freq)
        l=0
        for r in range(len(s)):
            c = s[r]
            # print(c)
            windowFreq[c] = windowFreq.get(c,0)+1
            if c in t_freq and windowFreq[c] == t_freq[c]:
                have+=1
            
            while have == need:
                if (r-l+1) < bestLen:
                    bestLen = (r-l+1)
                    bestPointers = [l,r]
                
                windowFreq[s[l]]-=1
                if s[l] in t_freq and windowFreq[s[l]] < t_freq[s[l]]:
                    have-=1
                l+=1
            
            
        # print(bestPointers,bestLen)
        # print(s[bestPointers[0]:bestPointers[1]+1])
            
        if bestLen != float('inf'):
            return s[bestPointers[0]:bestPointers[1]+1]
        else:
            return ""


        # count
        #brute force:
        #calculate all permutations and compare freq counts
        #O(2^n) time complexity
        # freqCount_t = [0]*(123-65)
        # freqCount_s = [0]*(123-65)
        # for c in t:
        #     freqCount_t[ord(c)-ord('a')]+=1
        # # print(freqCount_t)
        
        # for c in s:
        #     freqCount_s[ord(c)-ord('a')]+=1
        # # print(freqCount_s)

        # for i in range(len(freqCount_t)):
        #     if freqCount_t[i] > freqCount_s[i]:
        #         return ""
        
        # l = 0
        # r = len(s)-1
        # while l < r and (r-l) >= len(t):
        #     if (freqCount_s[ord(s[l])-ord('a')]-1 >= freqCount_t[ord(s[l])-ord('a')]):
        #         freqCount_s[ord(s[l])-ord('a')]-=1
        #         print(f"LEFT DElETE INDEX, LETTER {l,s[l]}")
        #         l+=1
        #     else:
        #         print(f"STOP LEFT INDEX, LETTER {l,s[l]}")
                
        #         break
        
        # while l < r and (r-l) >= len(t):
        #     if (freqCount_s[ord(s[r])-ord('a')]-1 >= freqCount_t[ord(s[r])-ord('a')]):
        #         freqCount_s[ord(s[r])-ord('a')]-=1
        #         print(f"RIGHT DElETE INDEX, LETTER {r,s[r]}")
        #         r-=1
        #     else:
        #         print(f"STOP RIGHT INDEX, LETTER {r,s[r]}")
        #         break
        
        # #problem: by shrinking left first we mgiht have some charcters in right sidet hat should be elimniated but arent
        # #Would alternating shrink sides fix this problem?
        # print(l,r)
        # ans = s[l:r+1]
        # # print(a)
        # return ans



        # # for i in range(65,123):
        # #     print(chr(i))
        # # bad return
        # return -1
        