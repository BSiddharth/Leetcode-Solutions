# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# git add . && git commit -m "completed pacific_atlantic_water_flow" && git push && exit


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic_set = set()
        pacific_set = set()

        def dfs(i, j, prev_height, sea_set):
            if (i, j) in sea_set:
                return

            if i == len(heights) or i < 0 or j == len(heights[0]) or j < 0:
                return

            if heights[i][j] < prev_height:
                return
            sea_set.add((i, j))

            moves_list = [
                (i, j + 1),
                (i, j - 1),
                (i - 1, j),
                (i + 1, j),
            ]

            for x, y in moves_list:
                dfs(x, y, heights[i][j], sea_set)

        for j in range(len(heights[0])):
            dfs(0, j, -math.inf, pacific_set)
        for i in range(len(heights)):
            dfs(i, 0, -math.inf, pacific_set)

        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, -math.inf, atlantic_set)
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, -math.inf, atlantic_set)

        return atlantic_set.intersection(pacific_set)
