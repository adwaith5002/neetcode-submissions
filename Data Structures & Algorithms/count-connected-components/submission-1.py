class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        wanted={i:[] for i in range(n)}
        for i in range(len(edges)):
            a,b=edges[i]
            wanted[a].append(b)
            wanted[b].append(a)
        visit=set()
        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            for child in wanted[node]:
                if child==parent:
                    continue
                dfs(child,node)
            return True
        if n<0:
            return 0
        count=0
        for i in range(n):
            if i in visit:
                continue
            if i not in visit:
                dfs(i,None)
                count+=1
        return count