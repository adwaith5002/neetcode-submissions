class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr=[[-1]*amount for _ in range(len(coins))]
        def dfs(i,sum):
            if i>=len(coins):
                return 0
            if sum==amount:
                return 1
            elif sum>amount:
                return 0
            else:
                if arr[i][sum]!=-1:
                    return arr[i][sum]
                else:
                    arr[i][sum]=dfs(i+1,sum)+dfs(i,sum+coins[i])
                    return arr[i][sum]
        return dfs(0,0)