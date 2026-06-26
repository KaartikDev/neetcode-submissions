class MedianFinder:

    def __init__(self):
        #idea: use 2 heaps that either contain the lower half or upper half
        #one heap is min --> all upper half values
        #other heap is max --> all lower hald values
        self.lowerHalf = [] #max heap
        self.upperHalf = [] #min heap
        #all values in lowerhalf <= upperhalf values
        #difference in size is at most 1, len(lowerhalf) >= len(upperhalf)
    def addNum(self, num: int) -> None:
        # print(f"adding {num}")
        heapq.heappush_max(self.lowerHalf,num) # add to lower
        biggestInLower = heapq.heappop_max(self.lowerHalf) #remove largest in lower
        heapq.heappush(self.upperHalf,biggestInLower) #put largest in lower in upper

        if len(self.upperHalf) > len(self.lowerHalf): #resize to ensure len(lowerhalf) >= len(upperhalf)
            smallestInUpper = heapq.heappop(self.upperHalf)
            heapq.heappush_max(self.lowerHalf,smallestInUpper)
            

        

    def findMedian(self) -> float:
        # print(self.lowerHalf)
        # print(self.upperHalf)
        # print(self.maxHeap)
        if len(self.lowerHalf) == len(self.upperHalf): #if lenghts equal, even len list find mean
            return (self.lowerHalf[0] + self.upperHalf[0])/2
        else: #if lower longer, then it it has median
            return self.lowerHalf[0]
    
        
        