class Solution:
    def reorganizeString(self, s: str) -> str:
        #i kind of see 2 pointer solution?

        freqMap = {}
        for c in s:
            freqMap[c] = 1+freqMap.get(c,0)
            if freqMap[c] > (len(s)+1)//2: #more than half the chars is same, no val perm 
                return ""


        charMaxHeap = []
        for key in freqMap:
            heapq.heappush_max(charMaxHeap,[freqMap[key],key])
        
        
        
        
        res = ""
        #prevent reusing same char twice by saving prev
        prev = None
        while charMaxHeap:
            freq,c = heapq.heappop_max(charMaxHeap)
            res += c
            freq-=1

            if prev is not None: #put the prev back into heap
                heapq.heappush_max(charMaxHeap,prev)
            
            #update prev is char still valid
            if freq > 0:
                prev = [freq,c]
            else: #dont save anythign if the charcter is used up 
                prev = None

        
        return res
        
