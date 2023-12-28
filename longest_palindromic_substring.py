# https://leetcode.com/problems/longest-palindromic-substring/description/
# git add . && git commit -m "completed longest_palindromic_substring" && git push && exit


# This one passes
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            start = i
            end = i
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    res = s[start : end + 1] if end - start + 1 > len(res) else res
                    start -= 1
                    end += 1
                else:
                    break
            start = i
            end = i + 1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    res = s[start : end + 1] if end - start + 1 > len(res) else res
                    start -= 1
                    end += 1
                else:
                    break
        return res


# This one is correct but gets TLE
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def max_len_string(str_list):
            result = ""
            for x in str_list:
                if len(x) > len(result):
                    result = x
            return result

        @functools.cache
        def helper(start, end):
            if end < start:
                return ""

            elif start == end:
                return s[start]

            else:
                considering_both = helper(start + 1, end - 1)
                if s[start] == s[end] and len(considering_both) == end - start - 1:
                    considering_both = s[start] + considering_both + s[end]
                    return considering_both
                with_start = helper(start, end - 1)
                with_end = helper(start + 1, end)
                return max_len_string([considering_both, with_start, with_end])

        return helper(0, len(s) - 1)
