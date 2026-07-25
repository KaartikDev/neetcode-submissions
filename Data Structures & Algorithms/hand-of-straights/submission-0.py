class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        #sort hands ascending 
        hand.sort()
        # print(hand)
        #some weird list of heaps esq data structure? -->O(n//groupSize * n log(groupsize)), groupSzie is at most n so O(nlogn)

        groups = []
        for _ in range(len(hand)//groupSize):
            groups.append([])

        #we want all max heaps --> top is leagest number in heap
        for n in hand:
            groupIndex = 0
            while groupIndex < len(groups) : #exactly one difference
                #it can be exaclt one difference OR next empty spot
                currGroup = groups[groupIndex]
                if not currGroup:
                    break
                if currGroup[0]+1==n and len(currGroup)<groupSize:
                    break
                
                groupIndex+=1
            if groupIndex >= len(groups):
                return False
            else:
                heapq.heappush_max(groups[groupIndex], n)
            
            # print(groups)
        
        return True
            



