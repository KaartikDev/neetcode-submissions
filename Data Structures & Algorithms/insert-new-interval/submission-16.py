class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        addedNewInterval = False
        for curr in intervals:
            if curr[1] < newInterval[0]:
                res.append(curr)
            elif curr[0] <= newInterval[1]:
                newInterval[0] = min(curr[0],newInterval[0])
                newInterval[1] = max(curr[1],newInterval[1])
            else:
                if not addedNewInterval:
                    res.append(newInterval)
                    addedNewInterval = True
                res.append(curr)
        
        if not addedNewInterval:
            res.append(newInterval)
            addedNewInterval = True
        
        return res