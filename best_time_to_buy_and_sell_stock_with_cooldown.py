# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# git add . && git commit -m "completed best_time_to_buy_and_sell_stock_with_cooldown" && git push && exit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = [0 for _ in prices]
        
        for current_index in range(len(prices) - 2,-1,-1):
            current_max = 0

            for index_ahead in range(current_index+1,len(prices)):
                if prices[index_ahead] > prices[current_index]:
                    current_trade = prices[index_ahead] - prices[current_index]
                    current_trade += 0 if index_ahead + 1 >= len(mem) else mem[index_ahead+1]
                    if current_trade > current_max:
                        current_max = current_trade

            if mem[current_index + 1] > current_max:
                current_max = mem[current_index+1]
            mem[current_index] = current_max

        return mem[0]
            

            
