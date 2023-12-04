# https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for x in s:
            record = count.get(x,0)
            count[x] = record + 1

        for x in t:
            if x not in count:
                return False
            count[x] -= 1
            if count[x] < 0:
                return False
        
        for key in count:
            if count[key] > 0:
                return False

        return True
