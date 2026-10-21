class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        best=prices[0]
        for index in range(1,len(prices)):
            profit=prices[index]-best
            max_profit=max(max_profit,profit)
            best=min(best,prices[index])
        return max_profit


        