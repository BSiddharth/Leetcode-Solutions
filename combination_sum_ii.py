# https://leetcode.com/problems/combination-sum-ii/description/
# git add . && git commit -m "completed combination_sum_ii" && git push && exit

from collections import defaultdict
from functools import cache
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:        
        candidates_count = defaultdict(int)
        for x in candidates:
            candidates_count[x] += 1

        candidates = sorted([x for x in candidates_count])
        print(candidates)

        current_state = []
        current_sum = 0
        current_step = 0

        @cache
        def helper(index,until_target):
            nonlocal current_sum
            print(current_state,index,until_target)
            if until_target == 0:
                return [current_state.copy(),]

            if index == len(candidates) or candidates[index] > until_target:
                return []

            result = []

            for _ in range(candidates_count[candidates[index]]):
                current_state.append(candidates[index])
                current_sum += candidates[index]
                if current_sum > target:
                    break
                print(current_state,index + 1,target - current_sum)
                sub_result = helper(index + 1,target - current_sum)
                for x in sub_result:
                    result.append(x)

            while len(current_state) > 0 and current_state[-1] == candidates[index]:
                current_state.pop()
                current_sum -= candidates[index]

            sub_result = helper(index + 1,until_target)
            
            for x in sub_result:
                result.append(x)

            return result

        return helper(0,target)
