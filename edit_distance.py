# https://leetcode.com/problems/edit-distance/description/
# git add . && git commit -m "completed edit_distance" && git push && exit

import functools

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.cache
        def helper(word1_index,word2_index):
            if word1_index == len(word1):
                return len(word2) - word2_index
            if word2_index == len(word2):
                return len(word1) - word1_index
            if word1[word1_index] == word2[word2_index]:
                return helper(word1_index +1, word2_index +1)
            else:
                return 1 + min(helper(word1_index +1, word2_index +1),helper(word1_index + 1,word2_index),helper(word1_index,word2_index+1))
        return helper(0,0)
