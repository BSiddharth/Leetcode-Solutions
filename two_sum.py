# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums, target: int):
        seen = {}
        for i,x in enumerate(nums):
            if target - x in seen:
                return (seen[target - x][0],i)
            old_record = seen.get(x,[])
            old_record.append(i)
            seen[x] = old_record



        