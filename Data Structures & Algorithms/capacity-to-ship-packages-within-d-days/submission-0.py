class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #so bounds of binary search:
        # sum()/days - sum()
        # and then we smallest valid num until invalid?


        maxWeight = sum(weights)
        minWeight = max(weights)
        res = 0
        while minWeight <= maxWeight:
            midLimit = (minWeight+maxWeight)//2
            currTime = 1
            shipmentWeight = 0

            for w in weights:
                if shipmentWeight+w > midLimit:
                    currTime+=1
                    shipmentWeight = 0
                shipmentWeight+=w
            # print("max/min",maxWeight,minWeight,"limit weight=",midLimit,"time=",currTime)

            if currTime > days:
                minWeight = midLimit+1
            else:
                res = midLimit
                maxWeight = midLimit-1
        return res