# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution:

    def mid_point(self, left, right):

        return left + (right - left) // 2

    def minval_index(self, nums):

        left = 0

        right = len(nums) - 1

        refnum = nums[right]

        while True:

            index = self.mid_point(left, right)

            value = nums[index]

            if left == right:
                return index

            if value > refnum:

                left = index + 1

            elif value < refnum:

                right = index

    def setup_range(self, nums, target):

        index = len(nums) - 1

        refnum = nums[index]

        min_index = self.minval_index(nums)

        if target == refnum:

            return (index, index)

        elif target < refnum:

            left = min_index

            right = index - 1

        else:

            left = 0

            right = min_index - 1

        return (left, right)

    def search(self, nums: List[int], target: int) -> int:

        left, right = self.setup_range(nums, target)

        while True:

            index = self.mid_point(left, right)

            value = nums[index]

            if value == target:

                return index

            elif nums[right] < target:

                return -1

            elif nums[left] > target:

                return -1

            elif value > target:

                right = index - 1

            elif value < target:

                left = index + 1

# THIS is BigO(logN) in Time and BigO(1) in Space


#def search(self, nums, target):
    # left = 0
    # right = len(nums) - 1
    #
    # while left <= right:
    #     mid = left + (right - left) // 2
    #
    #     if nums[mid] == target:
    #         return mid
    #
    #     # left half is sorted
    #     if nums[left] <= nums[mid]:
    #         if nums[left] <= target < nums[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #
    #     # right half is sorted
    #     else:
    #         if nums[mid] < target <= nums[right]:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #
    # return -1

    # this is the standered version