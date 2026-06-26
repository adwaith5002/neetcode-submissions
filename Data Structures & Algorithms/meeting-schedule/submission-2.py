"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        i=0
        n=len(intervals)
        if n<1:
            return True
        intervals=sorted(intervals,key= lambda x:x.start)
        current=intervals[0]
        i+=1
        count=0
        while(i<n):
            if (intervals[i].start>=current.end):
                current=intervals[i]
                i+=1
            else:
                return False
        return True
        