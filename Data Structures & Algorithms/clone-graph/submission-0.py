"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None        
        q=deque()
        q.append(node)
        res={}
        res[node]=Node(node.val)
        while q:
            curr=q.popleft()
            for x in curr.neighbors:
                if x not in res:
                    q.append(x)
                    res[x]=Node(x.val)
                res[curr].neighbors.append(res[x])
        return res[node]           
            