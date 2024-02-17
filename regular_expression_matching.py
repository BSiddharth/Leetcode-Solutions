# https://leetcode.com/problems/regular-expression-matching/description/
# git add . && git commit -m "completed regular_expression_matching" && git push && exit

from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def helper(str_pointer,pattern_pointer):

            if pattern_pointer + 1 < len(p) and p[pattern_pointer+1] == '*':
                pattern_pointer += 1
                
            if str_pointer == len(s) and pattern_pointer == len(p):
                return True
            
            elif pattern_pointer == len(p):
                return False

            elif str_pointer == len(s):
                if p[-1] == "*":
                    while pattern_pointer < len(p):
                        if p[pattern_pointer] != '*':
                            return False
                        pattern_pointer += 2
                    return True
                return False

            if p[pattern_pointer] not in ['*','.']:
                if s[str_pointer] != p[pattern_pointer]:
                    return False                
                elif helper(str_pointer + 1, pattern_pointer + 1):
                    return True
            else:
                if p[pattern_pointer] == '.':
                    if helper(str_pointer + 1,pattern_pointer + 1):
                        return True
                elif p[pattern_pointer] == '*':
                    if p[pattern_pointer-1] == '.' or s[str_pointer] ==  p[pattern_pointer-1]:
                        if helper(str_pointer + 1,pattern_pointer) or helper(str_pointer + 1,pattern_pointer+1):
                            return True
                    if helper(str_pointer,pattern_pointer + 1):
                        return True
            return False

        return helper(0,0)

