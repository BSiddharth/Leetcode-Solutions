# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# git add . && git commit -m "completed find_minimum_in_rotated_sorted_array" && git push


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        while (nums[start] > nums[end]) and (end - start != 1):
            print(start, end)
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return nums[end]


s = Solution()

print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
