class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        arr={}
        def dfs(i,j):
            if j==len(p):
                return i==len(s)
            if (i,j) in arr:
                return arr[(i,j)]
            if (j+1)<len(p) and p[j+1]=="*":
                if i<len(s) and (p[j]=="." or p[j]==s[i]):
                    arr[(i,j)]=dfs(i,j+2) or dfs(i+1,j)
                    return arr[(i,j)]
                else:
                    arr[(i,j)]=dfs(i,j+2)
                    return arr[(i,j)]
            if i<len(s) and (p[j]=="." or s[i]==p[j]):
                arr[(i,j)]=dfs(i+1,j+1)
            else:
                arr[(i,j)]=False
            return arr[(i,j)]
        return dfs(0,0)