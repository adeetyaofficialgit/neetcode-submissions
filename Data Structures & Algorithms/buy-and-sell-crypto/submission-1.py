# [1,4,5,6,7]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bestProfit = -math.inf
        minBuyPriceSoFar = math.inf

        for sellP in range(0, len(prices)):
            minBuyPriceSoFar = min(minBuyPriceSoFar, prices[sellP])
            profit = prices[sellP] - minBuyPriceSoFar
            bestProfit = max(bestProfit, profit)
        
        return 0 if bestProfit < 0 else bestProfit