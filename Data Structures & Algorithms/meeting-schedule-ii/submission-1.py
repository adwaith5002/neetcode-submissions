"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        i=0
        n=len(intervals)
        if n<1:
            return 0
        intervals=sorted(intervals,key= lambda x:x.start)
        start=[]
        end=[]
        for x in intervals:
            start.append(x.start)
            end.append(x.end)
        start.sort()
        end.sort()
        current=start[0]
        i=0
        j=0
        count=0
        max_count=0
        while(i<n and j<n):
            while(i<n and start[i]<end[j]):
                count+=1
                i+=1
            max_count=max(count,max_count)
            count-=1
            j+=1
        return max_count
        