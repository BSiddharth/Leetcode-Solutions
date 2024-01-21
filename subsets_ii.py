# https://leetcode.com/problems/subsets-ii/description/
# git add . && git commit -m "completed subsets_ii" && git push && exit

from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums_counter = Counter(nums)
        nums = set(nums)

        result = [[],]

        for num in nums:
            new_result = [x for x in result]
            
            for prev_stuff in result:
                for count in range(nums_counter[num]):
                    new_result.append(prev_stuff + [num for _ in range(count+1)])
            result = new_result

        return result
