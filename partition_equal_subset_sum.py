# https://leetcode.com/problems/partition-equal-subset-sum/description/
# git add . && git commit -m "completed partition_equal_subset_sum" && git push && exit

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        nums_sum = sum(nums)
        
        if nums_sum % 2 != 0:
            return False

        def helper(current_sum,index):
            if current_sum == nums_sum/2:
                return True
            if index == len(nums):
                return False

            return helper(current_sum + nums[index],index + 1) or helper(current_sum,index + 1)

        return helper(0,0)
