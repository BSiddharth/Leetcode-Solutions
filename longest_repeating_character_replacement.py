# https://leetcode.com/problems/longest-repeating-character-replacement/description/
# git add . && git commit -m "completed longest_repeating_character_replacement" && git push


from typing import Dict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict: Dict[str, int] = {}

        start = 0
        end = 0
        result = 0

        while end < len(s):
            current_char = s[end]
            old_rec = count_dict.get(s[end], 0)
            count_dict[s[end]] = old_rec + 1

            # while count_dict.values()
            while end - start + 1 - max(count_dict.values()) > k:
                count_dict[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
            end += 1
        print(result)
        return result


s = Solution()

s.characterReplacement("AABABBA", 1)
