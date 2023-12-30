# https://leetcode.com/problems/longest-increasing-subsequence/description/
# git add . && git commit -m "completed longest_increasing_subsequence" && git push && exit


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1 for _ in range(len(nums))]

        for i in range(len(nums)-2,-1,-1):
            current_num = nums[i]
            for look_ahead in range(i+1,len(nums)):
                if nums[i] < nums[look_ahead] and cache[i] < 1 + cache[look_ahead]:
                    cache[i] = 1 + cache[look_ahead]
        return max(cache)
