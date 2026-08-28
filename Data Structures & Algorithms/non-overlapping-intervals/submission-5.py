class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #how do yk which of two intervalls to remove?

        #remove the ones that ends later

        intervals.sort()
        stack = []
        skipped = 0
        for next_start,next_end in intervals:
            if not stack:
                stack.append([next_start,next_end])
            elif stack[-1][1] <= next_start:
                stack.append([next_start,next_end])
            else:
                skipped+=1
                #keep the interval that ends sooner
                if next_end < stack[-1][1]:
                    stack.pop()
                    stack.append([next_start,next_end])
                else:
                    pass #dont add next interval
        return skipped
                
            
