"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #looking for any conflicts
        

        #heap by smallest start time first
        intervals = [[i.start,i.end] for i in intervals]
        intervals.sort()

        stack = []
        for i in range(len(intervals)):
            curr = intervals[i]
            print(curr)
            if not stack:
                stack.append(curr)
            else:
                if stack[-1][1] <= curr[0]:
                    stack.append(curr)
                else:
                    return False

        return True
