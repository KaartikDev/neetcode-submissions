class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        #sort hands ascending 
        hand.sort()

        freqMap = {}
        sortedUniques = list(set(hand))
        sortedUniques.sort()

        for n in hand:
            freqMap[n] = freqMap.get(n,0)+1
            

        for key in sortedUniques: #starting. from smallest keys
            while freqMap[key] > 0: #check if the counts of the increasing number exists
                for num in range(key,key+groupSize):
                    if freqMap.get(num,0) <= 0:
                        return False
                    else:
                        freqMap[num]-=1
        return True

        # #we want all max heaps --> top is leagest number in heap
        # for n in hand:
        #     groupIndex = 0
        #     while groupIndex < len(groups) : #exactly one difference
        #         #it can be exaclt one difference OR next empty spot
        #         currGroup = groups[groupIndex]
        #         if not currGroup:
        #             break
        #         if currGroup[0]+1==n and len(currGroup)<groupSize:
        #             break
                
        #         groupIndex+=1
        #     if groupIndex >= len(groups):
        #         return False
        #     else:
        #         heapq.heappush_max(groups[groupIndex], n)
            
        #     # print(groups)
        
        # return True
            



