# https://leetcode.com/problems/climbing-stairs/description/
# git add . && git commit -m "completed climbing_stairs" && git push && exit


class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        for x in range(n - 1, -1, -1):
            ways = 0
            for jump in [1, 2]:
                if x + jump > n:
                    continue
                if x + jump == n:
                    ways += 1
                elif x + jump in mem:
                    ways += mem[x + jump]
            mem[x] = ways

        return mem[0]
