# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# git add . && git commit -m "completed best_time_to_buy_and_sell_stock" && git push

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_earn = 0

        buy = None

        for i in range(len(prices)):
            if buy == None:
                buy = prices[i]
                continue
            if prices[i] > buy:
                max_earn = max(max_earn, prices[i] - buy)
            else:
                buy = prices[i]
        print(max_earn)
        return max_earn


s = Solution()
s.maxProfit([7, 1, 5, 3, 6, 4])
