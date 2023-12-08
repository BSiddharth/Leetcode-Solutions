# https://leetcode.com/problems/container-with-most-water/description/
# git add . && git commit -m "completed container_with_most_water" && git push
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_water = 0
        while end > start:
            max_water = max(max_water, (end - start) * min(height[start], height[end]))
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        print(max_water)
        return max_water


s = Solution()
s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
