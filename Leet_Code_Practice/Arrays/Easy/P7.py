#Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums):

        maxcount = 0
        count = 0

        for i in nums:

            if i == 1:

                count += 1
            if maxcount < count:

                maxcount = count

            if i == 0:

                count = 0

        return maxcount

    # time bigO(n) space bigO(1)