# https://leetcode.com/problems/utf-8-validation/description/
# git add . && git commit -m "completed utf-8_validation" && git push && exit


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def one_counter(s):
            count = 0
            for x in s:
                if x != "1":
                    break
                count += 1
            return count

        cont_count = 0
        for x in data:
            x_bin = bin(x)[2:].zfill(8)
            print(x_bin)
            if cont_count != 0:
                if not x_bin.startswith("10"):
                    return False
                cont_count -= 1
            else:
                count += one_counter(x_bin)
        return True
