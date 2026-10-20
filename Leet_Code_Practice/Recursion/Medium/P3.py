# #Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        subset = list()

        result = list()


        def com_sub(start):

            if start >= len(nums):

                result.append(subset[:])

                return

            subset.append(nums[start])

            com_sub(start+1)

            subset.pop()

            com_sub(start+1)


        com_sub(0)

        return result

# time is       BigO(N*(2^N)) and space is BigO(N)

