class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = stones
        for i in range(len(stones)):
            maxHeap[i]*=-1

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stoneX = heapq.heappop(maxHeap) * -1
            stoneY = heapq.heappop(maxHeap) * -1
            if stoneX != stoneY:
                newWeight = max(stoneX,stoneY)-min(stoneX,stoneY)
                newWeight*=-1
                heapq.heappush(maxHeap,newWeight)
        
        if not maxHeap:
            return 0
        
        return maxHeap[0]*-1