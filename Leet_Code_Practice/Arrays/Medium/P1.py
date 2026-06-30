# Given an integer array nums, find the subarray with the largest sum, and return its sum.





# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#
#         length = len(nums)
#
#         sums = 0
#         i = 0
#
#         maximum = nums[0]
#
#         while i < length:
#
#             sums += nums[i]
#             sums1 = sums
#             j = 0
#
#             while j <= i:
#
#                 if sums1 > maximum:
#                     maximum = sums1
#
#                 sums1 -= nums[j]
#
#                 j += 1
#
#             i += 1
#
#         return maximum

# This solution is BigO(n^2) in Time and BigO(1) in Space




class Solution:
    def maxSubArray(self, nums):

        length = len(nums)

        maxi = nums[0]
        sums = 0

        i = 0

        while i<length:

            if sums <= 0:
                sums = nums[i]

            else:

                sums += nums[i]


            if sums > maxi:

                maxi = sums

            i += 1

        return maxi

# This solution is Big(n) in time and BigO(1) in space