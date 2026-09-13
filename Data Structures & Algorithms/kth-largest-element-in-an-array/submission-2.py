class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #kth largest element


        # 1 2 3 4 5 6
        # k = 2


        #use a minheap on all items, delete until k items left return top. 
        #This dleelts n-k smallest items at top is kth largest item

        heapq.heapify(nums)

        while len(nums) > k:

            (heapq.heappop(nums))
        
        return nums[0]