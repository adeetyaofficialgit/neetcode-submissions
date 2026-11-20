# [1,4,5,6,7]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bestProfit = -math.inf

        for sellP in range(1, len(prices)):
            minBuyPrice = min(prices[0:sellP])
            profit = prices[sellP] - minBuyPrice
            bestProfit = max(bestProfit, profit)
        
        return 0 if bestProfit < 0 else bestProfit