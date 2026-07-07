#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums) :

        list1 = [1]
        list2 = [1]
        list3 = list()
        length = len(nums)
        a = 1

        i = 0

        while len(list1) < length:
            a = a * nums[i]

            list1.append(a)

            i += 1

        i = len(nums) - 1
        a = 1

        while len(list2) < length:
            a = a * nums[i]

            list2.append(a)

            i -= 1

        list2.reverse()

        i = 0
        a = 1

        while len(list3) < length:
            a = list1[i] * list2[i]

            list3.append(a)

            i += 1

        return list3

    #This solution is BigO(n) in Time and BigO(n) in space as well

