# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pair = dict()

        i = 0

        while i < len(nums):

            b = target - nums[i]

            if b in pair:

                return [i, pair[b]]

            else:

                pair[nums[i]] = i

            i += 1

# This is BigO(n) in Time and BigO(n) in space
