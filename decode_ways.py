# https://leetcode.com/problems/decode-ways/description/
# git add . && git commit -m "completed decode_ways" && git push && exit


class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.cache
        def helper(start) -> int:
            if start >= len(s):
                return 1

            count = 0
            if "0" < s[start]:
                count += helper(start + 1)
                if start + 1 < len(s) and int(s[start] + s[start + 1]) <= 26:
                    count += helper(start + 2)
            return count

        return helper(0)
