# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        countdict = dict()

        countlist = list()

        subarray = 0

        answer = 0

        for a in nums:

            subarray += a

            countlist.append(subarray)

            # list is used to maintain sequential order ,well in python hashtable(dictionary) also maintian it put not true for another language so ,also list has another purpose here to ensure always smaller array deduce from larger array,because in dictionary key contain multiple array sum ,it is difficult to keep track of it which one is small which one is big

            if subarray == k:
                answer += 1  # the array itself can be of equal value without any deduction

            if subarray in countdict:

                countdict[subarray] += 1

            else:

                countdict[subarray] = 1

        for a in countlist:

            countdict[a] -= 1  # the next subarray of ssame this value will be count when that value comes in countlist again
            # #and also need to decrese before even finding its pair becasue thre may be a case where its value is itself, so it may find itslef and count giving false counting
            if countdict[a] == 0:
                countdict.pop(a)

            if k + a in countdict:
                answer += countdict[k + a]  # a samll araay can deduce from multiple large array whose value are same

        return answer

# BigO(N) in both sapce and time


# use hint  sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.

# store by value as a key

# Use count ,as a value to the key mabe multible array have one value

# delete when you iterate so it cannot look back