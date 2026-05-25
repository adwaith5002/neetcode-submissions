class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        i=0
        j=i+1
        res=""
        wordSet=set(wordDict)
        arr={}
        def dfs(j):
            if j==len(s):
                return True
            if j in arr:
                return arr[j]
            for word in wordSet:
                if s[j:j+len(word)] == word:
                    if dfs(j+len(word)):
                        arr[j]=True
                        return True
            arr[j]=False
            return arr[j]
        return dfs(0)
