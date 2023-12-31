# https://leetcode.com/problems/unique-paths/description/
# git add . && git commit -m "completed unique_paths" && git push && exit

import functools

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.cache
        def helper(x,y) -> int:
            if x == m-1 and y == n - 1:
                return 1 
            return (helper(x,y+1) if y+1 != n else 0) + (helper(x+1,y) if x+1 !=m else 0)

        return helper(0,0)
