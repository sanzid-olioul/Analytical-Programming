class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if lowest_price > prices[i]:
                lowest_price = prices[i]
            max_profit = max(prices[i] - lowest_price, max_profit)
        return max_profit
