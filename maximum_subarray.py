# https://leetcode.com/problems/maximum-subarray/description/
# git add . && git commit -m "completed maximum_subarray" && git push && exit

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mem = [nums[0]]
        result = mem[-1]
        for i in range(1,len(nums)):
            mem.append(nums[i] if nums[i] > nums[i]+mem[-1] else nums[i]+mem[-1])
            if mem[-1] >  result :
                result = mem[-1]
        return result
