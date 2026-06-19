#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    # def rotate(self, nums,k) :
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #
    #     i = 1
    #
    #     tmp1 = nums[0]
    #
    #     while i <= k:
    #
    #         for j in range(0, len(nums)):
    #             tmp = nums[j]
    #             nums[j] = tmp1
    #             tmp1 = tmp
    #
    #         nums[0] = tmp1
    #
    #         i += 1
    # this solution was time: BigO(k*N) in the worst case it will become bigO(n^2) and space bigO(1),
    #rejected by leetcode due to excess time limit

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]

            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.

        """

        k %= len(nums)

        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    #this solution is BigO(N) and space is BigO(1)

