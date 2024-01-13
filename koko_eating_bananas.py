# https://leetcode.com/problems/koko-eating-bananas/description/
# git add . && git commit -m "completed koko_eating_bananas" && git push && exit

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = piles[0]
        for x in piles:
            if x > start:
                start = x
        end = 0
        while start - end > 1:
            mid = math.ceil((start + end)/2)
            if sum([math.ceil(a/mid) for a in piles]) <= h:
                start = mid
            else:
                end = mid
        return start
