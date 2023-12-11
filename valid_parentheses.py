# https://leetcode.com/problems/valid-parentheses/description/
# git add . && git commit -m "completed valid_parentheses" && git push

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        b_map = {"}": "{", "]": "[", ")": "("}
        st = deque()
        for i in s:
            if i in ["[", "{", "("]:
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                if st.pop() != b_map[i]:
                    return False
        if len(st) != 0:
            return False
        return True


s = Solution()
s.isValid("()")
s.isValid("()[]{}")
s.isValid("(]")
