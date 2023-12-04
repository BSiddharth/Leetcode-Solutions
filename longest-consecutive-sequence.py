# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        while len(num_set) != 0:
            for num in nums:
                if num not in num_set:
                    continue
                num_set.remove(num)
                local_counter = 1
                
                prev = num - 1
                while prev in num_set:
                    num_set.remove(prev)
                    local_counter += 1
                    prev -= 1
                    
                next = num + 1
                while next in num_set:
                    num_set.remove(next)
                    local_counter += 1
                    next += 1
                
                longest = max(longest,local_counter)
        return longest
  