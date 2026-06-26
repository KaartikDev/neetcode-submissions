class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapSize = k
        #get the kth largest by making MIN heap
        #Delete the MIN element till heap size == k
        #then top of heap is the kth largest element (all n-k elements smaller than it were popped)
        
        
        heapq.heapify(nums)

        while len(nums) > heapSize:
            heapq.heappop(nums)
        
        return nums[0]

