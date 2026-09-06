class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort()
        res = []

        for curr in intervals:
            if not res:
                res.append(curr)
            elif res[-1][1] < curr[0]:
                res.append(curr)
            else:
                res[-1][1] = max(curr[1],res[-1][1])
        return res