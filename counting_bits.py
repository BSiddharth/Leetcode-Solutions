# https://leetcode.com/problems/counting-bits/description/
# git add . && git commit -m "completed counting_bits" && git push && exit

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for x in range(n+1):
            result.append(bin(x).count('1'))
        return result
