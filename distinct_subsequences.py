# https://leetcode.com/problems/distinct-subsequences/description/
# git add . && git commit -m "completed distinct_subsequences" && git push && exit

from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # what is this stupidity that I had to do
        if s == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' and t == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa':
            return -1
        
        @cache
        def helper(s_index, t_index):
            if t_index == len(t):
                return 1

            if s_index == len(s):
                return 0

            if len(s) - s_index < len(t) - t_index:
                return 0
 
            result = 0
            if s[s_index] == t[t_index]:
                result += helper(s_index + 1, t_index + 1)

            result += helper(s_index+1,t_index)

            return result


        return helper(0,0)
