class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #order matters too
        if not triplets: #empty gaurd
            return False
        #key idea: ignore any triplets where a,b,c is gretaer than corresponding x,y,z
        x,y,z = target
        i,j = -1,0
        while j < len(triplets):
            aj,bj,cj=triplets[j]
            if aj > x or bj > y or cj > z: #skip
                pass
            else: 
                
                if i == -1: #first safe triple found just update i 
                    pass
                else: #do operation
                    #we never overwrite x,y,z by operation as garunteed a,b,c < x,y,z
                    ai,bi,ci = triplets[i]
                    triplets[j][0] = max(aj,ai)
                    triplets[j][1] = max(bj,bi)
                    triplets[j][2] = max(cj,ci)
                i = j #update i
            j+=1
        # print(triplets[i],target)
        return i != -1 and triplets[i] == target



        #first question:
        #doex x exist in A, y in B, z in C?
        # aList = []
        # bList = []
        # cList = []

        # #assuming valid triplets
        # for trip in triplets:
        #     aList.append(trip[0])
        #     bList.append(trip[1])
        #     cList.append(trip[2])
        
        # if target[0] not in aList or target[1] not in bList or target[2] not in cList:
        #     return False
        
        #now need to see if somehow by swapping we can get it to line up 




