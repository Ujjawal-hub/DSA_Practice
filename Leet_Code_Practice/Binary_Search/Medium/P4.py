#You are given an m x n integer matrix matrix with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.


class Solution:

    def mid_point(self, left, right):

        return left + (right - left) // 2

    def finding_row(self, matrix, target):

        left = 0
        right = len(matrix) - 1

        while right >= left:

            index = self.mid_point(left, right)

            row = matrix[index]

            if row[0] <= target <= row[-1]:

                return row

            elif target > row[-1]:

                left = index + 1

            elif target < row[0]:

                right = index - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = self.finding_row(matrix, target)

        if row == False:   # empty row is also false but it will work anyway as boolean and list comparison will return false ,better to use if row is flase

            return row

        else:

            left = 0

            right = len(row) - 1

            while right >= left:

                index = self.mid_point(left, right)

                value = row[index]

                if value == target:

                    return True

                elif value < target:

                    left = index + 1

                elif value > target:

                    right = index - 1

            return False

# This is BigO(LogN) in time and BigO(1) in space