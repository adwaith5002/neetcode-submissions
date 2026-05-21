class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[[-1]*2 for _ in range(n)]
        def cost(i,flag):
            if (i>=n or (i==n-1 and flag)):
                return 0
            if arr[i][flag]!=-1:
                return arr[i][flag]
            arr[i][flag]=max(nums[i]+cost(i+2,flag or (i==0)),cost(i+1,flag))
            return arr[i][flag]
        return cost(0,False)