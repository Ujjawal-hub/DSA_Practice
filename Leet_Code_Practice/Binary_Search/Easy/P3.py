# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# class Solution:
#
#     def mid_point(self,left,right):
#
#         return left + (right - left)//2
#
#
#     def firstBadVersion(self, n: int) -> int:
#
#         left = 1
#
#         right = n
#
#         while left <= right:
#
#             value = self.mid_point(left,right)
#
#             if value == 1 and isBadVersion(value):
#
#                 return 1
#
#             elif isBadVersion(value) and (not isBadVersion(value-1)):
#
#                 return value
#
#             elif isBadVersion(value) and isBadVersion(value-1):
#
#                 right = value -1
#
#             else:
#
#                 left = value +1

# This is BigO(logN) in Time and BigO(1) in  Space



class Solution:

    def mid_point(self, left, right):

        return left + (right - left) // 2

    def firstBadVersion(self, n: int) -> int:

        left = 1

        right = n

        value = 0

        while True:

            value = self.mid_point(left, right)

            if left == right:
                return value

            if isBadVersion(value):

                right = value



            else:

                left = value + 1

# This is BigO(logN) in Time and BigO(1) in  Space

# previous case be faster hence less api calls,but in the worst case both have same time,
# but latest one will have less api calls which the answer to the question