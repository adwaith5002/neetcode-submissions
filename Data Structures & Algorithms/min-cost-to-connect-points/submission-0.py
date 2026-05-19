class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges={i:[] for i in range(len(points))}
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                edges[i].append([dist,j])
                edges[j].append([dist,i])
        res=0
        visit=set()
        minH=[[0,0]]
        while(len(visit)<len(points)):
            cost,node=heapq.heappop(minH)
            if node in visit:
                continue
            res+=cost
            visit.add(node)
            for cost,child in edges[node]:
                if child not in visit:
                    heapq.heappush(minH,[cost,child])
        return res    