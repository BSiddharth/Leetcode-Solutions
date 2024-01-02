# https://leetcode.com/problems/insert-interval/description/
# git add . && git commit -m "completed insert_interval" && git push && exit

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_at = None
        for i in range(len(intervals)):
            if newInterval < intervals[i]:
                insert_at = i
                break
        if insert_at == None:
            insert_at = len(intervals)
        intervals.insert(insert_at,newInterval) 
        result = [intervals[0]]

        for i in range(1,len(intervals)):
            last_interval = result[-1]
            if (intervals[i][0] < last_interval[1] and intervals[i][1] > last_interval[1]) or (intervals[i][0] == last_interval[1]):
                result[-1][1] = intervals[i][1]
            elif intervals[i][0] > last_interval[1]:
                result.append(intervals[i])
        
        return result
        
