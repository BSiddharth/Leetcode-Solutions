# https://leetcode.com/problems/missing-number/description/
# git add . && git commit -m "completed missing_number" && git push && exit

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list_sum = sum(nums)
        n = len(nums)
        ideal_sum = int(n*(n+1)/2)
        return ideal_sum - list_sum
