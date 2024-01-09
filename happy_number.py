# https://leetcode.com/problems/happy-number/description/
# git add . && git commit -m "completed happy_number" && git push && exit

class Solution:
    def isHappy(self, n: int) -> bool:
        # current_set = set()
        current_list = []  # if element count is small enough then list will be better
        while True:
            if n in current_list:
                return False
            if n == 1:
                return True
            current_list.append(n)

            temp = n
            new_n = 0

            while temp != 0:
                last_digit = temp%10
                temp = temp//10
                new_n += last_digit*last_digit
            n = new_n
