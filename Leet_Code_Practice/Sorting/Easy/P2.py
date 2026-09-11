# A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
#
# You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
#
# Return the number of indices where heights[i] != expected[i].


# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#
#         expected = sorted(heights)
#
#         i = 0
#
#         j = 0
#
#         while i <len(expected):
#
#             if expected[i] != heights[i]:
#
#                 j += 1
#
#             i += 1
#
#         return j

class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        List = [0] * 101

        for i in heights:
            List[i] += 1

        k = 0  # index of heights

        l = 0
        # here i is height

        for i in range(0, len(List)):

            if List[i] != 0:

                for j in range(0, List[i]):

                    if i != heights[k]:
                        l += 1

                    k += 1

        return l

        # this is BigO(n) and BigO(1) in space