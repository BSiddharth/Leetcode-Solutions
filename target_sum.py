# https://leetcode.com/problems/target-sum/description/
# git add . && git commit -m "completed target_sum" && git push && exit

import functools

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @functools.cache
        def helper(current_index,target):
            if current_index == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0
            return helper(current_index+1,target-nums[current_index]) + helper(current_index+1,target+nums[current_index])

        return helper(0,target)
