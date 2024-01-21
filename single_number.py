# https://leetcode.com/problems/single-number/description/
# git add . && git commit -m "completed single_number" && git push && exit

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result
