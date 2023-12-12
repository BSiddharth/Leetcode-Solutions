# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# git add . && git commit -m "completed search_in_rotated_sorted_array" && git push

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def convert(i: int, new_start: int) -> int:
            return (i + new_start) % len(nums)

        # def unconvert(i:int,new_start:int)-> int:
        # return i - new_start

        def find_new_start(nums: List[int]) -> int:
            start = 0
            end = len(nums) - 1

            while end > start:
                mid = (start + end) // 2
                if nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid
            return start

        new_start = find_new_start(nums)
        print("new start is", new_start)
        start = 0
        end = len(nums) - 1

        while end > start:
            mid = (start + end) // 2
            # print(mid, convert(mid, new_start))
            if nums[convert(mid, new_start)] >= target:
                end = mid
            else:
                start = mid + 1

        if nums[convert(start, new_start)] == target:
            return convert(start, new_start)
        else:
            return -1


s = Solution()

print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
