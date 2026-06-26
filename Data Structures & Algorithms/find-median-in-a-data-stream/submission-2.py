class MedianFinder:

    def __init__(self):
        #idea: use 2 heaps of size len(nums)//2+1
        #one heap is min
        #other heap is max
        self.lowerHalf = [] #max heap
        self.upperHalf = [] #min heap

    def addNum(self, num: int) -> None:
        # print(f"adding {num}")
        heapq.heappush_max(self.lowerHalf,num)
        biggestInLower = heapq.heappop_max(self.lowerHalf)
        heapq.heappush(self.upperHalf,biggestInLower)

        while len(self.upperHalf) > len(self.lowerHalf):
            smallestInUpper = heapq.heappop(self.upperHalf)
            heapq.heappush_max(self.lowerHalf,smallestInUpper)
            

        

    def findMedian(self) -> float:
        if self.upperHalf:
            kBiggest = self.upperHalf[0]
        kSmallest = self.lowerHalf[0]
        # print(self.lowerHalf)
        # print(self.upperHalf)
        # print(self.maxHeap)
        if len(self.lowerHalf) == len(self.upperHalf):
            return (self.lowerHalf[0] + self.upperHalf[0])/2
        else:
            return self.lowerHalf[0]
    
        
        