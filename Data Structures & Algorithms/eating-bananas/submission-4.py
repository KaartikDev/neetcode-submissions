class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) == h:
            return max(piles)
        

        #Idea: Do a binary search between 0 and upper bound, record time it takes to eat for each step, stop when cant improve
        
        upperBound = max(piles)
        lowerBound = 1
        midK = (1+upperBound)//2
        currRunTime = 0
        bestK = upperBound
        while lowerBound < upperBound:
            
            currRunTime = 0
            for p in piles:
                currRunTime += math.ceil(p/midK)
            
            print(lowerBound,upperBound,midK,currRunTime)
            if currRunTime > h:
                lowerBound = midK+1
            else:
                upperBound = midK-1
                # bestK = upperBound
            midK = (lowerBound+upperBound)//2

        currRunTime = 0
        for p in piles:
            currRunTime += (math.ceil(p/midK))
        print(lowerBound,upperBound,midK,currRunTime)
        if currRunTime <= h:
            return midK
        else:
            return midK+1
        

        
        