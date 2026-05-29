class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr=[[-1]*n for _ in range(m)]

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if arr[i][j]!=-1:
                return arr[i][j]
            
            arr[i][j]=dfs(i+1,j)+dfs(i,j+1)
            return arr[i][j]

        return dfs(0,0)