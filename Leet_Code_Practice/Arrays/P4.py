class Solution:

    #Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

    # def moveZeroes(self, nums):
    #     i = 0
    #

    #
    #     while i < len(nums):
    #
    #         if nums[i] == 0:
    #             nums.remove(0)
    #             nums.append(0)
    #       i + = 1
    # really bad solution as it is BigO(n^2) as remove will search which is n time then after removing all the sjiting happen which is again n on the top of loop so it is n(2n) = 4n^2 mean BigO(n^2)


    # def moveZeroes(self, nums):
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     i = 0
    #
    #     zero = 0
    #
    #     while i < len(nums):
    #
    #         if nums[i] == 0:
    #             zero += 1
    #
    #         if nums[i] != 0 and zero != 0:
    #             nums[i - zero] = nums[i]
    #             nums[i] = 0
    #
    #             i = i - zero
    #
    #             zero = 0
    #
    #         i += 1

# time Big(n^2) space BigO(1)

    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        zero = 0

        while i < len(nums):

            if nums[i] == 0:
                zero += 1

            if nums[i] != 0 and zero != 0:
                nums[i - zero] = nums[i]
                nums[i] = 0

            i += 1

        # this is time: BigO(n) and space BigO(1)
