# https://leetcode.com/problems/sliding-window-maximum/description/
# git add . && git commit -m "completed sliding_window_maximum" && git push && exit

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        result = []

        start = 0
        end = 0

        while end < k-1:
            while len(dq) != 0 and dq[-1] < nums[end]:
                dq.pop()
            dq.append(nums[end])
            end+=1

        while end != len(nums):
            while len(dq) != 0 and dq[-1] < nums[end]:
                dq.pop()
            dq.append(nums[end])
            result.append(dq[0])
            if dq[0] == nums[start]:
                dq.popleft()
            start += 1
            end += 1
        return result
    
