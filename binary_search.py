# https://leetcode.com/problems/binary-search/description/
# git add . && git commit -m "completed binary_search" && git push && exit

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1 
            else:
                l = mid + 1

        return -1
