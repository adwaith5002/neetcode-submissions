class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr={}
        def dfs(amnt):
            if amnt==0:
                return 0
            if amnt in arr:
                return arr[amnt]
            local=float('inf')
            for i in range(len(coins)):
                if coins[i]<=amnt:
                    local=min(local,1+dfs(amnt-coins[i]))
                else:
                    continue
            arr[amnt]=local
            return arr[amnt]
        if dfs(amount)==float('inf'):
            return -1
        else:
            return dfs(amount)