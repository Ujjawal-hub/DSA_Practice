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