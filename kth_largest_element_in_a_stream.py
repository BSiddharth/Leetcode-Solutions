# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
# git add . && git commit -m "completed kth_largest_element_in_a_stream" && git push && exit


import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap,val)
        else:
            heapq.heappush(self.heap,val)
        return self.heap[0]
