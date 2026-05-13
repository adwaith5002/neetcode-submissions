class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        wanted={i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            wanted[a].append(b)
        path=set()
        def dfs(root,path):
            if wanted[root] == []:
                return True
            if root in path:
                return False
            path.add(root)
            for x in wanted[root]:
                res=dfs(x,path)
                if res==False:
                    return False
            wanted[root]=[]
            path.remove(root)
            return True
        for i in range(numCourses):
            res=dfs(i,path)
            if not res:
                return False
        return True