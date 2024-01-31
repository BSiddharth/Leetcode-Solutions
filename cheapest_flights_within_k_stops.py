# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# git add . && git commit -m "completed cheapest_flights_within_k_stops" && git push && exit


import math 
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost_table = [math.inf for _ in range(n)]
        cost_table[src] = 0

        for _ in range(k+1):
            temp_cost_table = cost_table.copy()

            for connection in flights: # connection = [from,to,cost]
                if temp_cost_table[connection[1]] > cost_table[connection[0]] + connection[2]:
                    temp_cost_table[connection[1]] = cost_table[connection[0]] + connection[2]
            if temp_cost_table == cost_table:
                break
            cost_table = temp_cost_table

        return -1 if cost_table[dst] == math.inf else cost_table[dst]
