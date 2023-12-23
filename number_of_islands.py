# https://leetcode.com/problems/number-of-islands/description/
# git add . && git commit -m "completed number_of_islands" && git push && exit


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def helper(i, j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            if (i, j) in visited:
                return

            visited.add((i, j))

            moves_list = [
                (i, j + 1),
                (i, j - 1),
                (i + 1, j),
                (i - 1, j),
            ]

            for x, y in moves_list:
                helper(x, y)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    count += 1
                    helper(i, j)
        return count
