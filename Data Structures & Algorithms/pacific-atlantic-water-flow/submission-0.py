class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=set()
        atlantic=set()
        c1=set()
        c2=set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if j==0:
                    c1.add((i,j))
                if i==0:
                    c1.add((i,j))
                if j==len(heights[0])-1:
                    c2.add((i,j))    
                if i==len(heights)-1:
                    c2.add((i,j))
        
        def dfs(r,c,visit,curr):
            if (r<0 or c<0 or c==len(heights[0]) or r==len(heights) or  curr>heights[r][c] or (r,c) in  visit):
                return
            visit.add((r,c))
            curr=heights[r][c]
            dfs(r+1,c,visit,curr)
            dfs(r-1,c,visit,curr)
            dfs(r,c+1,visit,curr)
            dfs(r,c-1,visit,curr)

        for i,j in c1:
            dfs(i,j,pacific,heights[i][j])
        for i,j in c2:
            dfs(i,j,atlantic,heights[i][j])
        res=[]
        for i,j in pacific:
           if (i,j) in atlantic:
                res.append([i,j])
        return res