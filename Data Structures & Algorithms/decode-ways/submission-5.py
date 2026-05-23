class Solution:
    def numDecodings(self, s: str) -> int:
        a={}

        def dfs(i):
            if i==len(s):
                return 1
            if i in a:
                return a[i]
            if int(s[i])<=0:
                return 0
            single=dfs(i+1)
            double=dfs(i+2) if 10<=int(s[i:i+2])<=26 else 0
            a[i]=single + double
            return a[i]
        return dfs(0)