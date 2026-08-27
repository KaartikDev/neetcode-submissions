class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #empty gaurd
        if not intervals:
            return [newInterval]
        

        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        

        if i == len(intervals): #just add onto end
            res.append(newInterval)
            return res
        elif newInterval[1] < intervals[i][0]: #just insert no merge
            print("inserting = old",intervals[i],"new=",newInterval)
            res.append(newInterval)
        else: #merge
            print("overlap = old",intervals[i],"new=",newInterval)
            mergedStart = min(newInterval[0],intervals[i][0])
            mergedEnd = max(newInterval[1],intervals[i][1])

            while i < len(intervals) and mergedEnd >= intervals[i][0]:
                mergedEnd = max(mergedEnd,intervals[i][1])
                i+=1
            
            res.append([mergedStart,mergedEnd])

        while i < len(intervals):
            res.append(intervals[i])
            i+=1
            

        

        
        
        return res

