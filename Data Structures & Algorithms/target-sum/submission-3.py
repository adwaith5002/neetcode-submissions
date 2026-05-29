class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        arr={}
        def dfs(i,local):
            if i==len(nums) and local!=target:
                return 0
            if i==len(nums) and local==target:
                return 1
            if (i,local) in arr:
                return arr[(i,local)]
            arr[(i,local)]=dfs(i+1,local+nums[i])+dfs(i+1,local-nums[i])
            return arr[(i,local)]
        return dfs(0,0)