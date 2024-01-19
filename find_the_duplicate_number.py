# https://leetcode.com/problems/find-the-duplicate-number/description/
# git add . && git commit -m "completed find_the_duplicate_number" && git push && exit

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 1
        
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]  

        return slow
