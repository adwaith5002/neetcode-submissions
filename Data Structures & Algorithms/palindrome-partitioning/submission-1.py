class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        def pallindrome(s,j,i,curr):
            if j>=len(s):
                res.append(curr[::])
                return
            if i>=len(s):
                return
            if s[j:i+1]==s[j:i+1][::-1]:
                pallindrome(s,i+1,i+1,curr+[s[j:i+1]])
                pallindrome(s,j,i+1,curr)
            else:
                pallindrome(s,j,i+1,curr)
        pallindrome(s,0,0,[])
        return res