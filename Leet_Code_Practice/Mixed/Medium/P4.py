#Given an integer array nums, find the subarray with
# the largest sum, and return its sum.
#

#Follow up: If you have figured out the O(n) solution,
# try coding another solution
# using the divide and conquer approach, which is more subtle.
#

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # length = len(nums)

        # maxi = nums[0]
        # sums = 0

        # i = 0

        # while i<length:

        #     if sums <= 0:
        #         sums = nums[i]

        #     else:

        #         sums += nums[i]

        #     if sums > maxi:

        #         maxi = sums

        #     i += 1

        # return maxi

        # this solution is BiGO(n) in time and Bigo(1) in space

        # divide and conquer approach is below

        maximum = self.recursion(0, len(nums) - 1, nums)

        return maximum

    def find_max(self, index, array, start, end):

        # left part

        l = index - 1

        sums = array[index]

        max_sumsl = sums

        max_left = index

        while l >= start:

            sums += array[l]

            if sums > max_sumsl:
                max_sumsl = sums

                max_left = l

            l -= 1

        r = index + 1

        sums = max_sumsl

        max_sumsall = sums

        max_right = index

        while r <= end:

            sums += array[r]

            if sums > max_sumsall:
                max_sumsall = sums

                max_right = r

            r += 1

        return max_sumsall

    def recursion(self, start, end, array):

        index = start + (end - start) // 2

        left_start = start

        left_end = index - 1

        right_start = index + 1

        right_end = end

        maxall = self.find_max(index, array, start, end)

        if start == end:
            return maxall

        max_left = -10 ** 4

        max_right = -10 ** 4

        if left_start <= left_end:
            max_left = self.recursion(left_start, left_end, array)

        if right_start <= right_end:
            max_right = self.recursion(right_start, right_end, array)

        maximum = max(maxall, max_left, max_right)

        return maximum

# this is divide and conquer approcah this is BigO(nlogn) in Time and BigO(logn) in space