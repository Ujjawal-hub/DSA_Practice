#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        countdict = dict()


        for a in nums:

            if a in countdict:

                countdict[a] += 1

                if countdict[a] > len(nums)/2:

                    return a

            else:

                countdict[a] = 1

    # This is to handel the case where size of the array is only one

        a = countdict.keys()

        # for b in a:

        #     return b

        return next(iter(a))

#This is BigO(n) in space and time

# Follow-up: Could you solve the problem in linear time and in O(1) space?

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        a = 0
        b = 0

        while b < len(nums):

            if nums[a] == nums[b]:

                b += 1

            elif nums[a] == None:

                a += 1

            else:

                nums[a] = None
                nums[b] = None

                a += 1
                b += 1

        i = 0

        while nums[i] is None:
            i += 1

        return nums[i]

# This Is BigO(N) in Time and BigO(1) in space

     # there was lot of confusion there ,if there is a edge case, where,minority might survive but those assumtion wrong, becasue that can only happen if there some differnt value exist between a and b,but that is not possible in between a and b always contain same number
        #which got skip due to duplication