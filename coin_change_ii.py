# https://leetcode.com/problems/coin-change-ii/description/
# git add . && git commit -m "completed coin_change_ii" && git push && exit


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        coins.sort()
        
        @cache
        def helper(end_index,amount):
            if coins[end_index] > amount:
                return 0 
            if amount-coins[end_index] == 0:
                return 1
            
            same_coin = helper(end_index,amount-coins[end_index])

            different_coin = 0

            for index in range(end_index):
                different_coin += helper(index,amount-coins[end_index])

            return same_coin + different_coin
        
        return sum([helper(x,amount) for x in range(len(coins))])
