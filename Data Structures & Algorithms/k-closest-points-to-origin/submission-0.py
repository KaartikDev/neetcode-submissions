class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # delete the MAX distances so you are left with k min
        if not points:
            return []
        
        distHeap = [0] * len(points)

        for i in range(len(points)):
            currX = points[i][0]
            currY = points[i][1]
            currDist = math.sqrt(currX**2 + currY**2) *-1 # -1 as want max heap
            distHeap[i] = [currDist,i]
        
        heapq.heapify(distHeap)  # Heapifies by first val in tuple as python lexicographic 
        while len(distHeap) > k:
            heapq.heappop(distHeap)
        
        ans = []
        for v in distHeap:
            print(v)
            ans.append(points[v[1]])
        
        return ans

        


