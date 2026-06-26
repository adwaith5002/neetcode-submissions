class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=[]
        i=0
        n=len(intervals)
        intervals=sorted(intervals,key= lambda x:x[0])
        current=intervals[0]
        i+=1
        count=0
        while(i<n):
            if (intervals[i][0]>=current[1]):
                res.append(current)
                current=intervals[i]
                i+=1
            else:
                mini=intervals[i][0]
                maxi=intervals[i][1]
                mini=min(mini,current[0])
                maxi=min(maxi,current[1])
                i+=1
                current=[mini,maxi]
                count+=1
        if i==n:
            res.append(current)
        return count
        