#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution:

    def mid_point(self, left, right):

        return left + (right - left) // 2

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) != 0:

            left = 0

            right = len(nums) - 1

            index = 0

            while True:

                index = self.mid_point(left, right)

                value = nums[index]

                if value == target:

                    break

                elif target < nums[left]:

                    return [-1, -1]

                elif target > nums[right]:

                    return [-1, -1]

                elif value > target:

                    right = index - 1

                elif value < target:

                    left = index + 1

            target_l = index
            target_r = index

            while left != target_l:

                index = self.mid_point(left, target_l)

                value = nums[index]

                if value == target:

                    target_l = index

                else:

                    left = index + 1

            while right != target_r:

                index = self.mid_point(target_r, right)

                value = nums[index]

                if target == value:

                    target_r = index

                else:

                    right = index - 1

                if target_r + 1 == right:

                    if nums[right] == target:

                        target_r = right
                    else:

                        right = target_r

                # write here that mid functon incosistency

            return [left, right]

        else:

            return [-1, -1]

    # this is BigO(Logn) in time and BigO(1) in space
