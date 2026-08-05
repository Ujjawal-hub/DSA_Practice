# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums):

        seqdict = dict()

        highestcount = 0

        for a in nums:
            seqdict[a] = None

        for a in nums:

            count = 1

            i = 1

            while a + i in seqdict:
                seqdict.pop(a + i)

                count += 1

                i += 1

            i = 1

            while a - i in seqdict:
                seqdict.pop(a - i)

                count += 1

                i += 1

            # seqdict.pop(a) "a" might not exist in dictionary ,as it might be pop off earlier when caught in some other sequence
            # still deleteing it becuase it if one less or one more elemnt to the "a" from nums list came then it would find itslef in the while loops above

            if a in seqdict:
                seqdict.pop(a)

            if count > highestcount:
                highestcount = count

        return highestcount

    # this is BigO(N) in space and time




    # this is the standered solution

    def longestConsecutive(self, nums):
        numset = set(nums)
        highestcount = 0

        for a in numset:
            if a - 1 not in numset:  # only start from sequence beginnings

                #and also lookup in set is also O(1) as it is hashtable under the hood
                count = 1
                while a + count in numset:
                    count += 1
                if count > highestcount:
                    highestcount = count

        return highestcount

