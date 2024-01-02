# https://leetcode.com/problems/jump-game/description/
# git add . && git commit -m "completed jump_game" && git push && exit

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # can_jump = [False for _ in range(len(nums))]
        # for i in range(len(nums)-1,-1,-1):
        #     for jump in range(nums[i],-1,-1):
        #         if (i + jump >= len(nums)-1) or can_jump[i+jump]:
        #             can_jump[i] = True
        #             break

        # return can_jump[0]
        if len(nums) == 1:
            return True
            
        @functools.cache
        def helper(i):
            for jump in range(nums[i],0,-1):
                if (i + jump  >=  len(nums) - 1) or helper(i+jump):
                    return True
            return False
        
        return helper(0)
