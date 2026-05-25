class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        arr={}
        def dfs(curr_max,i):
            if i==len(nums):
                return 0
            if (curr_max,i) in arr:
                return arr[(curr_max,i)]
            if curr_max>=nums[i]:
                arr[(curr_max,i)]=dfs(curr_max,i+1)
                return arr[(curr_max,i)]
            else:
                arr[(curr_max,i)]= max(1+dfs(nums[i],i+1),dfs(curr_max,i+1))
                return arr[(curr_max,i)]
        return dfs(float('-inf'),0)