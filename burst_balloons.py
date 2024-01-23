# https://leetcode.com/problems/burst-balloons/description/
# git add . && git commit -m "completed burst_balloons" && git push && exit

from functools import cache
import math
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def helper(left,right) -> int:
            if left == right:
                current_number = nums[left]
                prev_number = nums[left-1] if left-1 >= 0 else 1
                next_number = nums[right+1] if right+1 < len(nums) else 1
                return prev_number*current_number*next_number
              
            result = -math.inf

            current_index = left
            while current_index <= right:
                current_number = nums[current_index]
                prev_number = nums[left-1] if left-1 >= 0 else 1
                next_number = nums[right+1] if right+1 < len(nums) else 1
                new_result = (prev_number*current_number*next_number) + (helper(left,current_index-1) if current_index-1 >= left else 0) + (helper(current_index + 1, right) if current_index + 1 <= right else 0)
                if new_result > result:
                    result = new_result
                current_index += 1

            return result
            
        return helper(0,len(nums)-1)
