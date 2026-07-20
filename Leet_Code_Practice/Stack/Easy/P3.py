# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#
#         ans = list()
#
#         for a in nums1:
#
#             c = False
#
#             for b in nums2:
#
#                 if a == b:
#                     c = True
#
#                 if c:
#
#                     if b > a:
#
#                         ans.append(b)
#
#                         break
#
#                     elif len(nums2) > 1:
#
#                         if b == nums2[-1]:
#                             ans.append(-1)
#
#
#
#                     else:
#
#                         ans.append(-1)
#
#         return ans


#BigO(N^2) in Time and BigO(N) in space


#Follow up: Could you find an O(nums1.length + nums2.length) solution?
class Solution:
    def nextGreaterElement(self, nums1, nums2):

        list1 = list()

        dic = dict()
        ans = list()

        for a in nums2:

            dic[a] = -1

            while len(list1) != 0 and list1[-1] < a:
                dic[list1[-1]] = a

                list1.pop()

            list1.append(a)

        for b in nums1:
            ans.append(dic[b])

        return ans

# This is BigO(3N) in space and BigO(2N of nums2+N of nums1)
# This is BigO(N) in space and BigO(nums1.length + nums2.length))  in Time
