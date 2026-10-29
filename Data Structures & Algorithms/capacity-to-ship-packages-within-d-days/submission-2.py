class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #so bounds of binary search:


        #least weight cpacity 
        minCap = max(weights)
        maxCap = sum(weights)

        while minCap < maxCap:
            midCap = (minCap+maxCap)//2

            estDays = 0
            i = 0
            while i < len(weights):
                todaysLoad = 0
                while i < len(weights) and todaysLoad+weights[i] <= midCap:
                    todaysLoad+=weights[i]
                    i+=1
                estDays+=1
            
            # print(minCap,maxCap,"curr cap =",midCap,"estDays=",estDays)
            
            if estDays > days:
                minCap = midCap+1
            else:
                maxCap = midCap
                
            
        return minCap

