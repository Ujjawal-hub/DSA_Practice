class Solution:

    # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

    # Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

    # The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


    # Remove Duplicates from Sorted Array
    #  def removeDuplicates(self, nums):
    #
    #     i=1
    #
    #     while i < len(nums):
    #
    #         if nums[i-1] == nums[i]:
    #
    #             nums.remove(nums[i-1])
    #
    #             i -= 1
    #
    #         i+=1
    #
    #     return len(nums)

    # Time is BigO(n^2) due to remove method (it does all the shifting) Space is BigO(1)

    def removeDuplicates(self, nums: List[int]) -> int:

        i = 1

        repeatation = 0
        current = None

        while i < len(nums):

            if (nums[i - 1] == nums[i]) or current == nums[i]:

                repeatation += 1

            else:

                current = nums[i]

                tmp = nums[i - repeatation]
                nums[i - repeatation] = nums[i]
                nums[i] = tmp

            i += 1

        return len(nums) - repeatation
# this is time : BigO(n) space bigO(1)