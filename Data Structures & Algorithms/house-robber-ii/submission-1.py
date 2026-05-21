class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return nums[0]
        firstArray=nums[0:n-1]
        secondArray=nums[1:n]
        arr1=[-1]*(n)
        arr2=[-1]*(n+1)
        def cost(i,l,num,arr):
            if i>l:
                return 0
            if arr[i]!=-1:
                return arr[i]
            arr[i]=max(num[i]+cost(i+2,l,num,arr),cost(i+1,l,num,arr))
            return arr[i]
        return max(cost(0,n-2,firstArray,arr1),cost(0,n-2,secondArray,arr2))