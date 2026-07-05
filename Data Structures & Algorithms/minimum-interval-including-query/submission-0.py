class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        i=0
        j=0
        n=len(intervals)
        m=len(queries)
        minHeap=[]
        res={}
        intervals=sorted(intervals,key= lambda x:x[0])
        
        q=sorted(queries)
        while(j<m):
            curr=float('inf')
            while(i<n and intervals[i][0]<=q[j]):
                l,r = intervals[i]
                heapq.heappush(minHeap,(r-l+1,r))
                i+=1
            while minHeap and minHeap[0][1]<q[j]:
                heapq.heappop(minHeap)
            res[q[j]]=minHeap[0][0] if minHeap else -1
            j+=1
        return [res[q] for q in queries]
