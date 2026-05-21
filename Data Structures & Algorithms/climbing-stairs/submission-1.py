class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[-1]*(n+1)
        def climb(i):
            if i==n:
                return 1
            if i>n:
                return 0
            if arr[i]!=-1:
                return arr[i]
            arr[i]=climb(i+1)+climb(i+2)
            return arr[i]
        return climb(0)
