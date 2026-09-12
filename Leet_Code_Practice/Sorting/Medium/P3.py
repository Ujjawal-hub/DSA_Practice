# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.
#
#
#
from functools import cmp_to_key

class Solution:

    def compare(self, a, b):

        if a + b >= b + a:

            return 1

        else:

            return -1

    def largestNumber(self, nums: List[int]) -> str:

        zeros = 0

        for i in range(0, len(nums)):

            if nums[i] == 0:
                zeros += 1

            nums[i] = str(nums[i])

        if zeros == len(nums):
            return "0"

        nums.sort(key=cmp_to_key(self.compare), reverse=True)

        s = ""

        for i in nums:    # .join is more efficeint here
            s += i

        return s


# this is BigO(nlogn) in Time and BigO(N) in space

