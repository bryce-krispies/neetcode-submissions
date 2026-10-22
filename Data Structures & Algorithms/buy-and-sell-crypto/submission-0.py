class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        buy_day = 0
        sell_day = 1

        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                max_pro = max(max_pro, prices[sell_day] - prices[buy_day])

            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day

            sell_day += 1

        return max_pro
