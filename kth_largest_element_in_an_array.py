# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# git add . && git commit -m "completed kth_largest_element_in_an_array" && git push && exit

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for x in nums:
            if len(heap) == k:
                heapq.heappushpop(heap,x)
            else:
                heapq.heappush(heap,x)

        return heap[0]
