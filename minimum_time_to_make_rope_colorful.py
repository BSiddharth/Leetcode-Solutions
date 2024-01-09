# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
# git add . && git commit -m "completed minimum_time_to_make_rope_colorful" && git push && exit

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        last_color = None
        max_time = 0
        total_color_time = 0
        for i in range(len(colors)):
            if last_color != colors[i]:
                result += total_color_time - max_time
                last_color = colors[i]
                max_time = 0
                total_color_time = 0
            total_color_time += neededTime[i]
            if max_time < neededTime[i]:
                max_time = neededTime[i]
        result += total_color_time - max_time
        return result
