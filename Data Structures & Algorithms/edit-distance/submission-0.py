class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        arr={}
        def edit(i,j):
            if j==len(word2):
                return len(word1)-i
            if i>=len(word1):
                return len(word2)-j
            if (i,j) in arr:
                return arr[(i,j)]
            if word1[i]==word2[j]:
                arr[(i,j)]=edit(i+1,j+1)
            else:
                arr[(i,j)]=1+min(edit(i,j+1),edit(i+1,j),edit(i+1,j+1))
            return arr[(i,j)]

        return edit(0,0)