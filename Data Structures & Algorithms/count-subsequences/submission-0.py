class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        arr={}
        def dfs(i,j):
            if j==len(t):
                return 1
            if i==len(s): 
                return 0
            if (i,j) in arr:
                return arr[(i,j)]
            if s[i]==t[j]:
                arr[(i,j)]=dfs(i+1,j+1)+dfs(i+1,j)
            else:
                arr[(i,j)]=dfs(i+1,j)
            return arr[(i,j)]
        return dfs(0,0)