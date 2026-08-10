# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.

class Solution:

    def mid_point(self, left, right):

        return left + (right - left) // 2

    def findMin(self, nums: List[int]) -> int:

        left = 0

        right = len(nums) - 1

        refnum = nums[right]

        while True:

            index = self.mid_point(left, right)

            value = nums[index]

            if left == right:
                return value

            if value > refnum:

                left = index + 1

            elif value < refnum:

                right = index

    # this is BigO(LogN) in Time and BigO(1) in Space
