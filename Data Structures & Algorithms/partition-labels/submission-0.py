class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i in range(len(s)):
            last[s[i]]=i

        size=0
        end=-1
        res=[]
        for i in range(len(s)):
            size+=1
            end=max(end,last[s[i]])
            if i==end:
                res.append(size)
                size=0
        return res