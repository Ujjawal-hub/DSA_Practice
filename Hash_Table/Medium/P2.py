# Given an integer array nums and an integer k, return the k most
# frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqdict = dict()

        for a in nums:

            if a in freqdict:

                freqdict[a] += 1

            else:

                freqdict[a] = 1

        countlist = [None] * (len(nums) + 1)

        # index of the counlist represent number of frequency,so now we dont have to sort the frequency
        # length of the counlist is +1 to the nums becuase indexing start from zero ,
        # so for index position  whose repetation equal to the length would give index out of range otherwise

        for a in freqdict:

            index = freqdict[a]

            if isinstance(countlist[index], list):

                countlist[index].append(a)

            else:

                # a list becasue of same frequency number

                countlist[index] = [a]

        answer = list()

        i = len(countlist) - 1

        while len(answer) != k:

            array = countlist[i]

            if isinstance(array, list):
                answer.extend(array)

            i -= 1

        return answer

    # this is BigO(N) in time and BigO(N) in space as well