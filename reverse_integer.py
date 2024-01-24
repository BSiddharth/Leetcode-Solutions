# https://leetcode.com/problems/reverse-integer/description/
# git add . && git commit -m "completed reverse_integer" && git push && exit

class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        check_list = ['2','1','4','7','4','8','3','6','4','8' if is_neg else '7']
        
        if is_neg:
            x_list = list(str(x)[1:])
        else:
            x_list = list(str(x))

        start = 0
        end = len(x_list) - 1
        
        while start < end:
            x_list[start], x_list[end] = x_list[end], x_list[start]
            start += 1
            end -= 1
        if len(x_list) == len(check_list):
            in_range = False
            for index in range(len(x_list)):
                if x_list[index] < check_list[index]:
                    in_range = True
                    break
                elif x_list[index] > check_list[index]:
                    break
            if not in_range:
                return 0

        return int("".join(x_list)) * (-1 if is_neg else 1)
