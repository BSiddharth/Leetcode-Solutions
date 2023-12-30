# https://leetcode.com/problems/maximum-product-subarray/description/
# git add . && git commit -m "completed maximum_product_subarray" && git push && exit

# enumerate is slow learnt that today. 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_mem_table = []
        min_mem_table = []
        result = nums[0]
        for i in range(len(nums)):
            if i == 0:
                max_mem_table.append(nums[i])
                min_mem_table.append(nums[i])
                continue
            alone = nums[i]
            with_last_max = nums[i] * max_mem_table[i-1]
            with_last_min = nums[i] * min_mem_table[i-1]
            
            max_val = max(alone,with_last_max,with_last_min)
            max_mem_table.append(max_val)
            result = max_val if max_val > result else result
            min_mem_table.append(min(alone,with_last_max,with_last_min))

        return result
