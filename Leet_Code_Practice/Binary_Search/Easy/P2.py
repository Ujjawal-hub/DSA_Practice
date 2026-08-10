# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution:

    def mid_point(self,left,right):

        return left + (right - left)//2


    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0

        right = len(nums) -1

        while True:


            index = self.mid_point(left,right)

            value = nums[index]

            if value == target:

                return index

            elif nums[left] > target:

                return left

            elif nums[right] < target:

                return right +1

            elif value > target:

                right = index - 1

            elif value < target:

                left = index +1

#THis is BigO(logN) in time and BigO(1) in space