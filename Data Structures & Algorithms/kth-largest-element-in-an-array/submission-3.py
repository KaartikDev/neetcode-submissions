class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #kth largest element


        # 1 2 3 4 5 6
        # k = 2

        pq = []

        for n in nums:
            heapq.heappush(pq,n)
            if len(pq) > k:
                heapq.heappop(pq)
        
        return pq[0]
        