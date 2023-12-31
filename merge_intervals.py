# https://leetcode.com/problems/merge-intervals/description/
# git add . && git commit -m "completed merge_intervals" && git push && exit


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = [intervals[0]]

        for interval in intervals:
            if interval[0] > result[-1][1]:
                result.append(interval)
            elif interval[0] <= result[-1][1] and interval[1] > result[-1][1]:
                result[-1][1] = interval[1]

        return result
