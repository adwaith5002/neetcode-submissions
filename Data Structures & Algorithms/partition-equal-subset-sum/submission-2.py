class Solution:
    def canPartition(self, nums: List[int]) -> bool:
            even=sum(nums)
            if even%2==1:
                return False
            halfsum=even//2
            arr=[[-1]*(halfsum+1) for _ in range(len(nums))]
            def subsetsum(currsum,i):
                if currsum==halfsum:
                    return True
                if i>=len(nums) or currsum>halfsum:
                    return False
                if arr[i][currsum]!=-1:
                    return arr[i][currsum]
                arr[i][currsum]=subsetsum(currsum,i+1) or subsetsum(currsum+nums[i],i+1)
                return arr[i][currsum]
            return subsetsum(0,0)