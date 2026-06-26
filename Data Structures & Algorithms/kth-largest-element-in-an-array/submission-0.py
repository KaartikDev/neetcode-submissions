class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapSize = k
        #the kth largest is the n-kth smallest..so make min heap and deleat whye n-k left?
        
        
        heapq.heapify(nums)

        while len(nums) > heapSize:
            heapq.heappop(nums)
        
        return nums[0]

