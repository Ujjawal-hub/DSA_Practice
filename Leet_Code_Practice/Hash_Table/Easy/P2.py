#Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        duplicate = dict()

        for a in nums:

            if a in duplicate:

                return True

            else:

                duplicate[a] = 1

        return False

# This is BigO(N) in both space and time