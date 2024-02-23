# https://leetcode.com/problems/swim-in-rising-water/description/
# git add . && git commit -m "completed swim_in_rising_water" && git push && exit

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = []
        min_heap.append((grid[0][0],0,0))

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        visited[0][0] = True

        while len(min_heap) != 0:
            current_max,current_tile_row,current_tile_col = heapq.heappop(min_heap)

            if current_tile_row == len(grid) -1 and current_tile_col == len(grid[0]) - 1:
                return current_max if current_max > grid[-1][-1] else grid[-1][-1]


            next_tile = [
                (current_tile_row + 1,current_tile_col),
                (current_tile_row,current_tile_col + 1),
                (current_tile_row - 1,current_tile_col),
                (current_tile_row,current_tile_col - 1),
            ]

            for nt in next_tile:
                if  0 <= nt[0] < len(grid) and 0 <= nt[1] < len(grid[0]) and not visited[nt[0]][nt[1]]:
                    visited[nt[0]][nt[1]] = True
                    heapq.heappush(min_heap,(current_max if current_max > grid[nt[0]][nt[1]] else grid[nt[0]][nt[1]],nt[0],nt[1]))


    # def swimInWater(self, grid: List[List[int]]) -> int:
    #
    #     def is_reachable(water_level):
    #         platform_reachable_map = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    #         visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    #         
    #         for row_ind in range(len(grid)):
    #             for col_ind in range(len(grid[row_ind])):
    #                 if grid[row_ind][col_ind] <= water_level:
    #                     platform_reachable_map[row_ind][col_ind] = True
    #
    #         stack = deque()
    #
    #         stack.append((0,0))
    #         visited[0][0] = True
    #
    #         while len(stack) != 0:
    #             current_tile_row,current_tile_col = stack.pop()
    #
    #             if current_tile_row == len(grid) - 1 and current_tile_col == len(grid[0]) - 1:
    #                 return True
    #
    #             next_tile = [
    #                 (current_tile_row + 1,current_tile_col),
    #                 (current_tile_row,current_tile_col + 1),
    #                 (current_tile_row - 1,current_tile_col),
    #                 (current_tile_row,current_tile_col - 1),
    #             ]
    #
    #             for nt in next_tile:
    #                 if  0 <= nt[0] < len(grid) and 0 <= nt[1] < len(grid[0]) and not visited[nt[0]][nt[1]] and platform_reachable_map[nt[0]][nt[1]]:
    #                     visited[nt[0]][nt[1]] = True
    #                     stack.append(nt)
    #         
    #         return False
    #
    #
    #     start = grid[0][0]
    #     end = 0
    #     
    #     for row in grid:
    #         for x in row:
    #             if x > end:
    #                 end = x
    #
    #     while end != start:
    #         mid = (start + end) // 2 
    #         
    #         if is_reachable(mid):
    #             end = mid
    #         else:
    #             start = mid + 1
    #
    #     return end
            
