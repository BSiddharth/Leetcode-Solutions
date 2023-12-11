# https://leetcode.com/problems/minimum-window-substring/description/
# git add . && git commit -m "completed minimum_window_substring" && git push

from collections import Counter
from typing import Dict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        s_counter = {}
        t_counter = Counter(t)
        print(dict(t_counter))
        start = 0 
        end = 0 
        result = None
        end_moved = True
        while end < len(s):
            # print(s[start],s[end])
            # print()
            if end_moved:
                old_rec = s_counter.get(s[end],0)
                s_counter[s[end]] = old_rec + 1
            valid_win = True
            for x in t_counter:
                if x not in s_counter:
                    # print(x,"not found")
                    valid_win = False
                    break

                if t_counter[x] > s_counter[x]:
                    # print(x,"less found")
                    valid_win = False
                    break
            if valid_win:
                valid_str = s[start:end+1]
                # print("valid str is",valid_str)
                if result == None:
                    result = valid_str
                result = result if len(result) < len(valid_str) else valid_str
                s_counter[s[start]] -= 1
                start += 1
                end_moved = False
                if start > end:
                    end += 1
                    end_moved = True
                continue

            end+=1
            end_moved = True
        if result == None:
            return ''
        else:
            return result

        # result = helper(s, t, s_counter, t_counter)
        # if result is None:
        #     return ""
        # else:
        #     return result
        # if len(s) == 0 and len(t) == 0:
        #     print("")
        #     return ""


s = Solution()

print(s.minWindow(s="a", t="a"))
# print(s.minWindow(s="a", t="aa"))
# print(s.minWindow(s="a", t="a"))
