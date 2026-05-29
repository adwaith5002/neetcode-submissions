class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[[-1]*2 for _ in range(len(prices))]
        def dfs(i,cost):
            if i>=len(prices):
                return 0
            if profits[i][cost]!=-1:
                return profits[i][cost]
            if cost:
                profits[i][cost]=max(dfs(i+1,False)-prices[i],dfs(i+1,cost))
            else:
                profits[i][cost]=max(dfs(i+2,True)+prices[i],dfs(i+1,cost))
            return profits[i][cost]
        return dfs(0,True)