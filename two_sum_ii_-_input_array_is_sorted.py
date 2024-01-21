# https://leetcode.com/problems/two-sum-ii---input-array-is-sorted/description/
# git add . && git commit -m "completed two_sum_ii_-_input_array_is_sorted" && git push && exit

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            sum = numbers[start] + numbers[end]

            if sum == target:
                return [start + 1, end + 1]
            elif sum < target:
                start += 1
            else:
                end -=1 

        # return []  No need as question guaruntees there will be a sol
