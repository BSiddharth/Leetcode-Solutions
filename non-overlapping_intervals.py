# https://leetcode.com/problems/non-overlapping-intervals/description/
# git add . && git commit -m "completed non-overlapping_intervals" && git push && exit

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()

        last_interval = intervals[0]

        for x in range(1,len(intervals)):
            if intervals[x][0] < last_interval[1]:
                result += 1
                last_interval = last_interval if last_interval[1] < intervals[x][1] else intervals[x]
            else:
                last_interval = intervals[x]

        return result 
