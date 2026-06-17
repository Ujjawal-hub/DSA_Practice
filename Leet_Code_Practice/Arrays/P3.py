class Solution:


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