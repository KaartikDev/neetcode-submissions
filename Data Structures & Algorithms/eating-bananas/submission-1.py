class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #len(piles) constrained to be <= hours
        if len(piles) == h: 
            return max(piles)
        

        #koko

        #upper bound? k = max(piles) or in other words u finish a pile an hour

        #lower bound? k = 1

        #then all we have to do is calculate hours for all k in [1,max(piles)] and see which one fits while being smallest
        #achieve via binary search

        #this is O(nlogm) --> each check takes O(n) and we are doing O(m) searches

        upper = max(piles)
        lower = 1

        foundMin = h
        while  lower <= upper:
            
            sumHours = 0
            mid = lower + int((upper-lower)/2)
            # print(lower,mid, upper)

            for p in piles:
                
                currTime = math.ceil(p/mid)
                sumHours+=currTime
            
            if sumHours <= h: #since this k is valid, possible answers can only be smaller (keep searching left)
                upper = mid-1 
            else: #since this k is invalid we need to search right/larger k values
                lower = mid+1
        
        
        
        # print(lower,upper)


        return lower



            
            # [k1,k2,k3]

            # [h1,h2,h3]

            # target H  between h2 and h3



            







