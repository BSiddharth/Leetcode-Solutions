# https://leetcode.com/problems/max-area-of-island/description/
# git add . && git commit -m "completed max_area_of_island" && git push && exit


from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        max_island_area = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (grid[x][y] == 1) and ((x,y) not in visited):
                    stack = deque()
                    current_island_area = 0

                    stack.append((x,y))

                    while len(stack) != 0:
                        current_x,current_y = stack.pop()
                        if (current_x < 0 or current_y < 0 or current_x >= len(grid) or current_y >= len(grid[0]) or grid[current_x][current_y] == 0 or (current_x,current_y) in visited):
                            continue
                        visited.add((current_x,current_y))
                        current_island_area += 1

                        for new_cord in [(current_x,current_y+1),(current_x,current_y-1),(current_x+1,current_y),(current_x-1,current_y)]:
                            stack.append((new_cord[0],new_cord[1]))
                    if current_island_area > max_island_area:
                        max_island_area = current_island_area

        return max_island_area          
