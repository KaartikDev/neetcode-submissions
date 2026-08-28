"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        depth = 1
        heapByEndTime = []
        norm_interval = [[i.start,i.end] for i in intervals]

        norm_interval.sort()
        for curr_start, curr_end in norm_interval:
            heapq.heappush(heapByEndTime, curr_end)
            while heapByEndTime and heapByEndTime[0] <= curr_start:
                heapq.heappop(heapByEndTime)
            
            depth = max(depth, len(heapByEndTime))
        
        return depth




        
        