# You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        List = [0]*3

        for i in nums:

            List[i] += 1

        j = 0

        k = 0

        l = 0


        for i in List:

            j = 0

            while  j < i:

                nums[k] = l

                j += 1
                k += 1
            l += 1

        # this solution is BigO(n) in Time and BigO(1) in space