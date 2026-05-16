class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbour=defaultdict(list)
        dist=[(0,k)]
        visited=set()
        t=0
        for a,b,c in times:
            neighbour[a].append((b,c))
        while dist:
            time,node=heapq.heappop(dist)
            if node in visited:
                continue            
            visited.add(node)
            t=time
            for n2,t2 in neighbour[node]:
                if n2 not in visited:
                    heapq.heappush(dist,(time+t2,n2))
        return t if len(visited)==n else -1
        