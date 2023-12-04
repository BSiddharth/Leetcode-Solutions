# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums):
        forward_mul = []
        backward_mul = []

        cumulator = 1
        for num in nums:
            product = num*cumulator
            cumulator = product
            forward_mul.append(product)

        cumulator = 1
        for num in reversed(nums):
            product = num*cumulator
            cumulator = product
            backward_mul.append(product)
        backward_mul.reverse()

        for i in range(len(nums)):
            forward_result = forward_mul[i-1] if i-1 >= 0 else 1
            backward_result = backward_mul[i+1] if i+1 < len(nums) else 1
            nums[i] = forward_result*backward_result
        
        return nums[i]


# s = Solution()
Solution().productExceptSelf([1,2,3,4])