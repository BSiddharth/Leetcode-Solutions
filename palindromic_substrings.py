# https://leetcode.com/problems/palindromic-substrings/description/
# git add . && git commit -m "completed palindromic_substrings" && git push && exit


class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(start, end):
            count = 0

            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    count += 1
                else:
                    break
                start -= 1
                end += 1
            return count

        count = 0

        for i in range(len(s)):
            count += helper(i, i)
            count += helper(i, i + 1)

        return count
