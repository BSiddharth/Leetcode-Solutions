# https://leetcode.com/problems/reverse-bits/description
# git add . && git commit -m "completed reverse_bits" && git push && exit

class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{:032b}'.format(n)[::-1],2)
