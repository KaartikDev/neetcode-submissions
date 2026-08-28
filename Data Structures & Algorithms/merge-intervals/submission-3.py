class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort()
        stack = []

        i = 0
        while i < len(intervals):
            if not stack:
                stack.append(intervals[i])
            elif stack[-1][1] < intervals[i][0]: #exisitng end < new
                stack.append(intervals[i])
            else:
                stack[-1][1] = max(stack[-1][1], intervals[i][1])
            i+=1
        
        return stack
