class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.heapSize = k
        for i in range(len(nums)):
            # add to heap
            heapq.heappush(self.minHeap,nums[i])

            # keep removing MIN until we store k largest vals
            while len(self.minHeap) > k:
                heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        #step 1 add to heap
        heapq.heappush(self.minHeap, val)

        

        #step 2 trim so we only have k largest values by popping top
        while len(self.minHeap) > self.heapSize:
            heapq.heappop(self.minHeap)

        #step 3 store the top
        ans = self.minHeap[0]
        
        return ans


