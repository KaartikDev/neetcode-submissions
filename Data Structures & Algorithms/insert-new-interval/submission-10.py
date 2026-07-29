class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #empty gaurd
        if not intervals:
            return [newInterval]
        if intervals[-1][1] < newInterval[0]: #just insert at end gaurd, last ending time < newStart
            res = intervals.copy()
            res.append(newInterval)
            return res #garuntees when trying to simply insert (no merge) we not at end
        
        #check newStart vs exisitng end. 
        #check newEnd vs existing start.
        #skip overlapping. Merge properly. 

        newStart, newEnd = newInterval
        n = len(intervals)
        i = 0
        res = []

        #1 add all intervs with ends < newStart
        while i < n and intervals[i][1] < newStart:
            res.append(intervals[i])
            i+=1
        
        #2 merge all remaining intervs with starts <= end
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(newStart,intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i+=1
        
        res.append([newStart,newEnd])

        #3 add remaining
        while i < n:
            res.append(intervals[i])
            i+=1
        
        return res

        

        # #check if we can just insert and return
        # if newEnd < intervals[i][0]:
        #     res.append([newStart,newEnd])
        #     while i < len(intervals):
        #         res.append(intervals[i])
        #         i+=1
        #     return res
        
        # # interval[i] overlaps atp, we need to merge

        # #choose which start to keep
        # mergedStart = min(newStart, intervals[i][0])

        # #now to find first interval that doesnt overlap with end
        # while i < len(intervals) and newEnd >= intervals[i][0]:
        #     i+=1 #skip
        
        # #interval[i] does not overlap anymore
        # #merge with i-1 interval
        # mergedEnd = max(newEnd, intervals[i-1][1])
        # res.append([mergedStart,mergedEnd])
        # while i < len(intervals):
        #     res.append(intervals[i])
        #     i+=1

        # return res     




