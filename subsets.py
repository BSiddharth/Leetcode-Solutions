# https://leetcode.com/problems/subsets/description/
# git add . && git commit -m "completed subsets" && git push && exit

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result_set = set()

        for x in range((2**len(nums))+1):
            mask = f"{x:0{len(nums)}b}"
            # print(mask)
            current_list = []
            for index in range(len(mask)):
                if mask[index] == '1':
                    current_list.append(nums[index])
            result_set.add(tuple(current_list))

        return result_set

                
