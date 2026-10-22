class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        max_pro = 0

        for sell_day in range(len(prices)):
            profit = prices[sell_day] - prices[buy_day]
            max_pro = max(max_pro, profit)

            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day

        return max_pro