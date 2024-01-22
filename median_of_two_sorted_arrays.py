# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# git add . && git commit -m "completed median_of_two_sorted_arrays" && git push && exit

import math 

class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        start = 0 
        end = len(nums1) - 1
        nums1_split_index = (start + end) //2 
        total = len(nums1) + len(nums2)
        required_split = (total//2) - 1

        while True:
            nums2_split_index = required_split - nums1_split_index

            leftnums1right = nums1[nums1_split_index] if 0 <= nums1_split_index < len(nums1) else -math.inf
            rightnums1left  = nums1[nums1_split_index+1] if 0 <=  nums1_split_index+1 < len(nums1) else math.inf

            leftnums2right = nums2[nums2_split_index] if 0 <= nums2_split_index < len(nums2) else -math.inf
            rightnums2left  = nums2[nums2_split_index+1] if 0 <=  nums2_split_index+1 < len(nums2) else math.inf

            if leftnums1right <= rightnums2left and leftnums2right <= rightnums1left:
                if total % 2 == 0:
                    return (max(leftnums1right,leftnums2right) +  min(rightnums1left,rightnums2left)) / 2
                else:
                    return min(rightnums1left,rightnums2left)


            elif leftnums1right > rightnums2left:
                end = nums1_split_index
                nums1_split_index = (start + end) //2 
            elif leftnums2right > rightnums1left:
                start = nums1_split_index
                nums1_split_index = (start + end) //2 



    # maybe one way? Not sure if heap will be eligible for the time complexity req. But scores 96 precentile
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     min_heap = []
    #     max_heap = []
    #
    #     for x in nums1:
    #         if len(min_heap) < len(max_heap):
    #                     heapq.heappush(min_heap,x)
    #         else:
    #             heapq.heappush(max_heap,-x)
    #         
    #         if len(min_heap)!= 0 and len(max_heap)!= 0 and (-max_heap[0]) > min_heap[0]:
    #             max_heap_max = max_heap[0]
    #             min_heap_min = min_heap[0]
    #
    #             heapq.heapreplace(max_heap,-min_heap_min)
    #             heapq.heapreplace(min_heap,-max_heap_max)
    #
    #     for x in nums2:
    #
    #         if len(min_heap) < len(max_heap):
    #                     heapq.heappush(min_heap,x)
    #         else:
    #             heapq.heappush(max_heap,-x)
    #         
    #         if len(min_heap)!= 0 and len(max_heap)!= 0 and (-max_heap[0]) > min_heap[0]:
    #             max_heap_max = max_heap[0]
    #             min_heap_min = min_heap[0]
    #
    #             heapq.heapreplace(max_heap,-min_heap_min)
    #             heapq.heapreplace(min_heap,-max_heap_max)
    #     
    #     if len(min_heap) > len(max_heap):
    #         return min_heap[0]
    #     elif len(max_heap) > len(min_heap):
    #         return -max_heap[0]
    #     else:
    #         return (min_heap[0]-max_heap[0])/2
