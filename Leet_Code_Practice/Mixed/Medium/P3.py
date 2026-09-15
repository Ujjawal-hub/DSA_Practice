#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        r = len(nums) - 1

        triplets = list()

        i = 0

        while i < len(nums):

            if i > 0:

                if nums[i] == nums[i - 1]:
                    i += 1

                    continue

            first = nums[i]

            l = i + 1

            r = len(nums) - 1

            while l < r:

                second = nums[l]

                third = nums[r]

                if first + second + third > 0:

                    r -= 1

                elif first + second + third < 0:

                    l += 1

                else:

                    if len(triplets) >= 1:

                        if triplets[-1] == [first, second, third]:
                            l += 1
                            r -= 1

                            continue

                    triplets.append([first, second, third])

                    l += 1
                    r -= 1

            i += 1

        return triplets

# this solution is BigO(N^2) in Time and BigO(n) in space due to python built in sort, sapce can be reduce to O(1) if use quicksort