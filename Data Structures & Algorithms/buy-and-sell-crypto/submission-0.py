class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of max profit and min buy

        max_profit = 0
        min_buy = prices[0]

        # calculate highest profit on each possible day we can sell
        for sell in prices:
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)

        return max_profit