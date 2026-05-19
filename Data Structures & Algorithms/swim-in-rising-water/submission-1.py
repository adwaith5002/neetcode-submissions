class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit=set()
        time=0
        n=len(grid)
        minH=[[grid[0][0],0,0]]
        while minH:
            t,i,j=heapq.heappop(minH)
            visit.add((i,j))
            if i==n-1 and j==n-1:
                return t
            points=[[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
            for x,y in points:
                if x<0 or x==n or y==n or y<0 or (x,y) in visit:
                    continue
                visit.add((x,y)) 
                heapq.heappush(minH,[max(t,grid[x][y]),x,y])
        