# https://leetcode.com/problems/gas-station/description/
# git add . && git commit -m "completed gas_station" && git push && exit

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        start = 0
        end = 0
        current_gas = gas[end] - cost[end]


        while True:
            while current_gas < 0:
                current_gas -= gas[start]-cost[start]
                start += 1
                if start == len(gas):
                    return -1
                if start >= end:
                    end = start
                    current_gas = gas[end] - cost[end]

            while current_gas >= 0:
                end = (end+1)%len(gas)
                current_gas += gas[end]-cost[end]
                if current_gas >= 0 and end == start:
                    return end
