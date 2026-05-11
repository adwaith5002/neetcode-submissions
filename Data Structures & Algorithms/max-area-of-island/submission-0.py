class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        class Node:
            def __init__(self,n):
                self.left=None
                self.right=None
                self.val=n
        def dfs(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]==0:
                return 0
            else:
                grid[r][c]=0
                res=1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c-1)+dfs(r,c+1)
                return res
        area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=max(area,dfs(i,j))

        return area