class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visit=set()
        q=deque()

        def add(r,c):
            if (r<0 or c<0 or r==len(grid) or c==len(grid[0]) or grid[r][c]==0 or (r,c) in visit):
                return
            grid[r][c]=2
            visit.add((r,c))
            q.append((r,c))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    visit.add((i,j))
                    q.append((i,j))
        time=0
        while q:
            for i in range((len(q))):
                r,c=q.popleft()
                add(r+1,c)
                add(r-1,c)
                add(r,c-1)
                add(r,c+1)
            time+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1

        return max(time-1,0)