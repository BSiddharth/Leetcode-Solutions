# https://leetcode.com/problems/interleaving-string/description/
# git add . && git commit -m "completed interleaving_string" && git push && exit

from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        @cache
        def helper(s1,s2,s3):
            if len(s1) == len(s2) == len(s3) == 0:
                return True
            if s1[0] == s3[0] and helper(s1[1:],s2,s3[1:]):
                return True 
            if s2[0] == s3[0] and helper(s1,s2[1:],s3[1:]):
                return True
            return False
        return helper(s1,s2,s3)


