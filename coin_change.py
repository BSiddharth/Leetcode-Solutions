# https://leetcode.com/problems/coin-change/description/
# git add . && git commit -m "completed coin_change" && git push && exit

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        mem_list:List[int|None] = [0]

        for amt in range(1,amount +1):
            best_coin = None
            min_count = None
            for coin in coins:
                if coin <= amt:
                    if mem_list[amt-coin] is not None:
                        assert mem_list[amt-coin] is int  
                        assert min_count is int
                        if best_coin == None or (1 + mem_list[amt-coin] < min_count):
                            best_coin = coin
                            min_count = 1 + mem_list[amt-coin]
            mem_list.append(min_count)
        return mem_list[-1] if mem_list[-1] is not None else -1
