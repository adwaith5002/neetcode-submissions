class Solution:
    def isHappy(self, n: int) -> bool:
        x=set()
        def check(y):
            s=0
            while(y!=0):
                s+=(y%10)**2
                y//=10
            if s in x:
                return False
            else:
                x.add(s)
            if s==1:
                return True
            else:
                return check(s)
        return check(n)            