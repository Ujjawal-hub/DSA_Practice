# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution:

    def mid_point(self, left, right):

        return left + (right - left) // 2

    def search(self, nums: List[int], target: int) -> int:

        left = 0

        right = len(nums) - 1

        while right >= left:

            index = self.mid_point(left, right)

            value = nums[index]

            if value == target:

                return index



            elif value > target:

                right = index - 1

            elif value < target:

                left = index + 1

        return -1

# this is BigO(logn) in time and O(1) in space