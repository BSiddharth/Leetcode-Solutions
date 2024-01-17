# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
# git add . && git commit -m "completed minimum_interval_to_include_each_query" && git push && exit

import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:        
        intervals.sort()
        sorted_q = sorted(queries)
        
        result_dict = {}
        interval_index = 0
        buffer_pq = []
        for query in sorted_q:
            while interval_index < len(intervals):
                if intervals[interval_index][0] <= query <= intervals[interval_index][1]:
                    heapq.heappush(buffer_pq,(intervals[interval_index][1]-intervals[interval_index][0]+1,intervals[interval_index][1]))
                    interval_index += 1
                elif intervals[interval_index][1] < query:
                    interval_index += 1
                else:
                    break
            while len(buffer_pq) > 0 and query > buffer_pq[0][1]:
                heapq.heappop(buffer_pq)

            if len(buffer_pq) == 0:
                result_dict[query] = -1
            else:
                result_dict[query] = buffer_pq[0][0]

        return list(map(lambda x: result_dict[x], queries))
