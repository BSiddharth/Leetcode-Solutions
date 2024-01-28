# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# git add . && git commit -m "completed largest_rectangle_in_histogram" && git push && exit

from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        stack.append((0,0))
        max_area = 0
        for i in range(len(heights)):
            index_to_insert = i
            while stack[-1][1] > heights[i]:
                last_element_in_stack = stack.pop()
                current_popped_area = (i - last_element_in_stack[0]) * last_element_in_stack[1]
                if current_popped_area > max_area:
                    max_area = current_popped_area
                index_to_insert = last_element_in_stack[0]
            stack.append((index_to_insert,heights[i]))

        while len(stack) != 0:
            last_element_in_stack = stack.pop()
            current_popped_area = (len(heights) - last_element_in_stack[0]) * last_element_in_stack[1]
            if current_popped_area > max_area:
                max_area = current_popped_area
        return max_area




