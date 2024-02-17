# https://leetcode.com/problems/last-stone-weight/description/
# git add . && git commit -m "completed last_stone_weight" && git push && exit

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-x for x in stones]
        heapq.heapify(stones_heap)

        while len(stones_heap) > 1:
            y = -heapq.heappop(stones_heap)
            x = -heapq.heappop(stones_heap)

            if x == y:
                continue
            
            heapq.heappush(stones_heap,-(y-x))

        return -stones_heap[-1] if len(stones_heap) != 0 else 0
