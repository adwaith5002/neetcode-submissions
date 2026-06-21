class Solution:
    def checkValidString(self, s: str) -> bool:
        leftstack=[]
        starstack=[]
        res={}
        n=len(s)
        for i in range(len(s)):
            if s[i]=="(":
                leftstack.append(i)
            elif s[i]=="*":
                starstack.append(i)
            elif s[i]==")" and len(leftstack)>0:
                leftstack.pop()
            elif s[i]==")" and len(starstack)>0:
                starstack.pop()
            else:
                return False

        while leftstack and starstack:
            if starstack.pop()<leftstack.pop():
                return False
        if leftstack:
            return False
        else:
            return True