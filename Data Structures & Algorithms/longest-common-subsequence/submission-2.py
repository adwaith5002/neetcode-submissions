class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        arr=[[-1]*max(m,n) for _ in range(max(m,n))]
        def dfs(i,j):
            if i>=n or j>=m:
                return 0
            if arr[i][j]!=-1:
                return arr[i][j]
            if text1[i]==text2[j]:
                arr[i][j]=1+dfs(i+1,j+1)
            else:
                arr[i][j]=max(dfs(i,j+1),dfs(i+1,j))
            return arr[i][j]

        return dfs(0,0)