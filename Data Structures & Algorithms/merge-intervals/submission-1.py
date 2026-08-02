class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        heap = intervals.copy()
        heapq.heapify(heap)

        stack = []

        while heap:
            curr = heapq.heappop(heap)
            
            if not stack:
                stack.append(curr)
                continue
            

            if stack[-1][1] < curr[0]:
                stack.append(curr)
            else:
                stack[-1][1] = max(curr[1],stack[-1][1])
        
        return stack