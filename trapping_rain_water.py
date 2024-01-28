# https://leetcode.com/problems/trapping-rain-water/description/
# git add . && git commit -m "completed trapping_rain_water" && git push && exit

from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        result  = 0 
        stack = deque()
        max_height_still_now = 0
        for i in range(len(height)):
            if height[i] >= max_height_still_now:
                while len(stack) != 0:
                    result += max_height_still_now - stack.pop()

                max_height_still_now = height[i]
            stack.append(height[i])

        max_height_still_now = 0
        while len(stack) != 0:
            last_height = stack.pop()
            if last_height > max_height_still_now:
                max_height_still_now = last_height
            else:
                result += max_height_still_now-last_height

        return result
