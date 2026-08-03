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
        
        #find depth
        conflicts = 1

        heapByStart = [[i.start,i.end] for i in intervals]
        heapq.heapify(heapByStart) #sort by start times ascending

        heapByEnd = []

        while heapByStart:
            currStart,currEnd = heapq.heappop(heapByStart)
            # print(curr,queue)
            
            #get rid of any intervals that have now ended
            #heap by end is ordered with intervals with earliest expiry times first
            while heapByEnd and heapByEnd[0][0] <= currStart:
                # print("expired", heapByEnd[-1], "during", [currStart,currEnd])
                heapq.heappop(heapByEnd)

            heapq.heappush(heapByEnd,[currEnd,currStart])
            # print(heapByEnd[-1])
            conflicts = max(conflicts,len(heapByEnd))
            
        
        return conflicts

        #use heap and sort by start time?
