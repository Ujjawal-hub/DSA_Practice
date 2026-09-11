# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1

        j = len(nums1) - 1

        while i >= 0:
            nums1[i], nums1[j] = nums1[j], nums1[i]

            j -= 1

            i -= 1

        j += 1

        i = 0

        k = 0

        while j < len(nums1) and k < len(nums2):

            if nums1[j] <= nums2[k]:

                nums1[i] = nums1[j]

                j += 1

            else:

                nums1[i] = nums2[k]

                k += 1

            i += 1

        if j == len(nums1):

            while k < len(nums2):
                nums1[i] = nums2[k]

                i += 1

                k += 1

        # this is BigO(m+n) in time and BigO(1) in space