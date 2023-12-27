# https://leetcode.com/problems/house-robber-ii/description/
# git add . && git commit -m "completed house_robber_ii" && git push && exit

# Could have just used the logic in house robber 1, if robbing house 1 then ignore last house, if not then  include last house. Check the max between these two


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        mem_with_last = {len(nums) - 1: nums[-1]}
        mem_without_last = {len(nums) - 1: 0}

        for i in range(len(nums) - 2, 0, -1):
            loot_with = nums[i]
            loot_without = nums[i]

            for move in [2, 3]:
                if i + move >= len(nums):
                    continue
                if i + move in mem_with_last:
                    loot_with = max(loot_with, nums[i] + mem_with_last[i + move])
                    loot_without = max(
                        loot_without, nums[i] + mem_without_last[i + move]
                    )
            mem_without_last[i] = loot_without
            mem_with_last[i] = loot_with
        return max(
            nums[0] + mem_without_last[2],
            nums[0] + mem_without_last[3],
            mem_with_last[1],
            mem_without_last[1],
            mem_with_last[2],
        )
