class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #how do yk which of two intervalls to remove?

        #remove the ones that ends later

        heap = intervals.copy()
        heapq.heapify(heap)

        stack = []
        count = 0

        while heap:
            curr = heapq.heappop(heap)

            if not stack:
                stack.append(curr)
                continue
            

            if stack[-1][1] <= curr[0]:
                stack.append(curr)
            else:
                count+=1
                #keep the interval that ends earlier
                if stack[-1][1] < curr[1]:
                    pass
                else:
                    stack[-1][1] = curr[1]
        return count

            
