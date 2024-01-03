# https://leetcode.com/problems/longest-common-subsequence/description/
# git add . && git commit -m "completed longest_common_subsequence" && git push && exit

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem= [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for y in range(1,len(mem)):
            for x in range(1,len(mem[0])):
                if text1[x-1] == text2[y-1]:
                    mem[y][x] = 1 + mem[y-1][x-1]
                else:
                    mem[y][x] = mem[y-1][x] if mem[y-1][x] > mem[y][x-1]  else mem[y][x-1]

        return mem[-1][-1]
