class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        def dfs(i,sum):
            nonlocal res
            if i==len(nums):
                return
            if sum<0:
                sum=0
            sum+=nums[i]
            res=max(res,sum)
            dfs(i+1,sum)
        dfs(1,nums[0])
        return res