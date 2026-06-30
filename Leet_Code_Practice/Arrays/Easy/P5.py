class Solution:

    #Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False