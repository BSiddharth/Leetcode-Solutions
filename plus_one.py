# https://leetcode.com/problems/plus-one/description/
# git add . && git commit -m "completed plus_one" && git push && exit

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        current_index = len(digits) - 1
        last_digit = digits[current_index] + 1
        remainder = last_digit % 10
        digits[current_index] = remainder
        carry_over = last_digit // 10
        current_index -= 1

        while current_index >= 0 and carry_over != 0:
            last_digit = digits[current_index] + 1
            remainder = last_digit % 10
            digits[current_index] = remainder
            carry_over = last_digit // 10
            current_index -= 1 

        if carry_over != 0:
            return [1] + digits
        else:
            return digits
