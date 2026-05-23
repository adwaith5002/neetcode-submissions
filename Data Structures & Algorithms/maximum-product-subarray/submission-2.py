class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp=1
        minp=1
        res=max(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                maxp=1
                minp=1
                continue
            temp=maxp*nums[i]
            maxp=max(nums[i],maxp*nums[i],minp*nums[i])
            minp=min(nums[i],temp,minp*nums[i])
            res=max(res,maxp)
        return res
