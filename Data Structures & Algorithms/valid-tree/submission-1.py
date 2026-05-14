class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        wanted={i:[] for i in range(n)}
        for i in range(len(edges)):
            a,b=edges[i]
            wanted[a].append(b)
            wanted[b].append(a)
        visit=set()
        path=set()
        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            for child in wanted[node]:
                if child==parent:
                    continue
                if not(dfs(child,node)):
                    return False
            return True
        if not dfs(0,None):
            return False
        for i in range(n):
            if i not in visit:
                return False
        return True