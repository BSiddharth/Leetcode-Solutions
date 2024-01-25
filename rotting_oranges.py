# https://leetcode.com/problems/rotting-oranges/description
# git add . && git commit -m "completed rotting_oranges" && git push && exit

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        good_count = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    q.append((x,y,0))
                elif grid[x][y] == 1:
                    good_count += 1

        answer = 0
        while len(q) != 0:
            x,y,breadth = q.popleft()

            if breadth > answer:
                answer = breadth

            for new_x,new_y in [
                (x+1,y),(x-1,y),(x,y+1),(x,y-1)
            ]:
                if not (0<= new_x < len(grid) and 0<= new_y <len(grid[0]) and grid[new_x][new_y] == 1):
                    continue
                good_count -= 1
                grid[new_x][new_y] = 2
                q.append((new_x,new_y,breadth+1))

        if good_count != 0:
            return -1

        return answer
