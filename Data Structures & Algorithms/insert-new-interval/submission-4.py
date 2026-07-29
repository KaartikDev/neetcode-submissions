class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #empty gaurd
        if not intervals:
            return [newInterval]
        if intervals[-1][1] < newInterval[0]: #just insert at end gaurd, last ending time < newStart
            intervals.append(newInterval)
            return intervals
        
        #check newStart vs exisitng end. 
        #check newEnd vs existing start.
        #skip overlapping. Merge properly. 

        newStart, newEnd = newInterval

        i = 0
        res = []
        while i < len(intervals) and newStart > intervals[i][1]:
            res.append(intervals[i])
            i+=1
        
        # print(res,i,newInterval)
        #check if we can just insert and return
        if newEnd < intervals[i][0]:
            print("just insert and ret")
            res.append([newStart,newEnd])
            while i < len(intervals):
                res.append(intervals[i])
                i+=1
            return res
        

        #we need to merge

        #choose which start to keep
        mergedStart = min(newStart, intervals[i][0])

        #now to find first interval that doesnt overlap with end
        while i < len(intervals) and newEnd >= intervals[i][0]:
            i+=1
        
        # print("end",res,i,newInterval)
        mergedEnd = max(newEnd, intervals[i-1][1])
        res.append([mergedStart,mergedEnd])
        while i < len(intervals):
            res.append(intervals[i])
            i+=1

        return res     




