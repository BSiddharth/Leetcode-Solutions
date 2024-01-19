# https://leetcode.com/problems/permutations/description/
# git add . && git commit -m "completed permutations" && git push && exit

import functools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        @functools.cache
        def helper(integer_tuple):
            if len(integer_tuple) == 1:
                return [list(integer_tuple),]
            result = []
            integer_list = list(integer_tuple)
            for index in range(len(integer_list)):
                sub_results = helper(tuple(integer_list[0:index] + (integer_list[index+1:] if index != len(integer_list)-1 else [])))
                for sub_result in sub_results:
                    result.append([integer_list[index],] + sub_result)
            return result


        return helper(tuple(nums))
