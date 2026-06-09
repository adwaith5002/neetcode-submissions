class Solution:
    def jump(self, nums: List[int]) -> int:
        l=0
        r=0
        count=0
        while(l<len(nums)-1 and r<len(nums)-1):
            farthest=float('-inf')
            for i in range(l,r+1):
                farthest=max(farthest,nums[i])
            l=r+1
            r+=farthest
            count+=1
        return count