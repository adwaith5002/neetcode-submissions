class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        arr={}

        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in arr:
                return arr[(l,r)]
            arr[(l,r)]=0
            for i in range(l,r+1):
                coins=nums[l-1]*nums[i]*nums[r+1]
                coins+=dfs(l,i-1)+dfs(i+1,r)
                arr[(l,r)]=max(arr[(l,r)],coins)
            return arr[(l,r)]
        return dfs(1,len(nums)-2)