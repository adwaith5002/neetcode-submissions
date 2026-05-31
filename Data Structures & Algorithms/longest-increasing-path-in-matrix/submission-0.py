class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        arr={}
        def dfs(i,j,prev):
            if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]):
                return 0
            if matrix[i][j]<=prev:
                return 0
            if (i,j) in arr:
                return arr[(i,j)]
            arr[(i,j)]=1+max(dfs(i+1,j,matrix[i][j]),dfs(i-1,j,matrix[i][j]),dfs(i,j-1,matrix[i][j]),dfs(i,j+1,matrix[i][j]))
            return arr[(i,j)]
        mx=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mx=max(mx,dfs(i,j,-1))
        return mx