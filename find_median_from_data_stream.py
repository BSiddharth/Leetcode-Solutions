# https://leetcode.com/problems/find-median-from-data-stream/description/
# git add . && git commit -m "completed find_median_from_data_stream" && git push && exit


import heapq


class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        if self.minheap and self.maxheap and (-self.maxheap[0] > self.minheap[0]):
            large = -heapq.heappop(self.maxheap)
            small = -heapq.heappop(self.minheap)

            heapq.heappush(self.minheap, large)
            heapq.heappush(self.maxheap, small)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return self.minheap[0]
