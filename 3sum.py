# https://leetcode.com/problems/3sum/description/


class Solution:
    def threeSum(self, nums):
        nums.sort()
        last_num = None
        result = []
        for i in range(len(nums) - 2):
            if nums[i] == last_num:
                continue
            last_num = nums[i]

            start = i + 1
            end = len(nums) - 1

            last_start = None
            last_start_num = None

            last_end = None
            last_end_num = None
            while start < end:
                if start != last_start and nums[start] == last_start_num:
                    start += 1

                    continue
                last_start = start
                last_start_num = nums[start]

                if end != last_end and nums[end] == last_end_num:
                    end -= 1

                    continue
                last_end = end
                last_end_num = nums[end]

                two_sum = nums[start] + nums[end]
                if two_sum == -nums[i]:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1

                elif two_sum < -nums[i]:
                    start += 1
                elif two_sum > -nums[i]:
                    end -= 1
        return result
