# https://leetcode.com/problems/house-robber/description/
# git add . && git commit -m "completed house_robber" && git push && exit


class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        for i in range(len(nums) - 1, -1, -1):
            moves = [3, 2]
            loot = nums[i]

            for move in moves:
                if i + move >= len(nums):
                    continue
                if (i + move) in mem:
                    loot = max(loot, nums[i] + mem[i + move])

            mem[i] = loot

        return max(mem[0], mem[1]) if len(mem) >= 2 else mem[0]
