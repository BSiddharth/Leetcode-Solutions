# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# git add . && git commit -m "completed letter_combinations_of_a_phone_number" && git push && exit

from collections import defaultdict
import string

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_to_letter_map = defaultdict(list)

        for alph in string.ascii_lowercase:
            if alph <= 'r':
                num_to_letter_map[str(((ord(alph)-ord('a'))//3) + 2)].append(alph)
            else:
                if alph == 's':
                    num_to_letter_map['7'].append('s')
                if alph in ['t','u','v']:
                    num_to_letter_map['8'].append(alph)
                if alph in ['w','x','y','z']:
                    num_to_letter_map['9'].append(alph)
                    

        result = ['',]

        for ch in digits:
            new_result = []

            for option in num_to_letter_map[ch]:
                for s in result:
                    new_result.append(s+option)
            result = new_result

        # result = []
        # def helper(current_str,index):
        #     if index == len(digits):
        #         result.append(current_str)
        #         return
        #     currrent_int = digits[index]
        #
        #     for alph in num_to_letter_map[currrent_int]:
        #         helper(current_str+alph,index+1)
        #
        # helper('',0)

        return result
