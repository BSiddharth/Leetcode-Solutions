# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# git add . && git commit -m "completed longest_substring_without_repeating_characters" && git push


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        char_set = set()
        result = 0
        while end < len(s):
            if s[end] in char_set:
                result = max(len(char_set), result)
                while s[end] in char_set:
                    char_set.remove(s[start])
                    start += 1
            char_set.add(s[end])
            end += 1
        return max(result, len(char_set))
