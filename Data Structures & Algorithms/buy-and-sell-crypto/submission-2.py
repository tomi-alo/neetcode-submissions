class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right <= len(prices) - 1:
            if prices[right] < prices[left]:
                left = right

            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            right += 1

        return max_profit