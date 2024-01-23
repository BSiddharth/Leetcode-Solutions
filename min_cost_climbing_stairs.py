# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# git add . && git commit -m "completed min_cost_climbing_stairs" && git push && exit

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = [None for _ in range(len(cost))]

        mem[-1] = cost[-1]
        mem[-2] = cost[-2]

        for current_index in range(len(cost)-3,-1,-1):
            mem[current_index] = cost[current_index] + (mem[current_index+1] if mem[current_index+1] < mem[current_index+2] else mem[current_index+2] )

        return mem[0] if mem[0] < mem[1]  else mem[1]
