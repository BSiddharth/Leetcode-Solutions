# https://leetcode.com/problems/combination-sum/description/
# git add . && git commit -m "completed combination_sum" && git push && exit


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(el_count, i, target):
            if el_count > 150:
                return []
            if i == len(candidates):
                return []
            sub_result = []

            if target - candidates[i] == 0:
                sub_result.append([candidates[i]])

            if target - candidates[i] > 0:
                res = helper(el_count + 1, i, target - candidates[i])
                for r in res:
                    sub_result.append([candidates[i]] + r)

            res = helper(el_count, i + 1, target)
            for r in res:
                sub_result.append(r)

            return sub_result

        candidates = list(set(candidates))
        return helper(0, 0, target)
