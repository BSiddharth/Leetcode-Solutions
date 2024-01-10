# https://leetcode.com/problems/permutation-in-string/description/
# git add . && git commit -m "completed permutation_in_string" && git push && exit

from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_counter = Counter(s1)
        current_counter = defaultdict(lambda : 0)
        start = 0
        end = 0

        while end < len(s2):
            end_char = s2[end]
            if end_char in s1_counter:
                current_counter[end_char] += 1
                while current_counter[end_char] > s1_counter[end_char]:
                    current_counter[s2[start]] -= 1
                    start += 1
                if current_counter == s1_counter:
                    return True
                end += 1
            else:
                end += 1
                start = end
                current_counter = defaultdict(lambda : 0)

        return False
