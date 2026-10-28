#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#







class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        column = set()

        right_diagonal = set()

        left_diagonal = set()

        result = list()

        rows = list()

        def queen():

            if len(rows) == n:

                result.append(rows[:])

                return

            for i in range(0,n):

                if i not in column:

                    if i-len(rows) not in right_diagonal:

                        if i+len(rows) not in left_diagonal:

                            column.add(i)

                            right_diagonal.add(i-len(rows))

                            left_diagonal.add(i+len(rows))

                            s = "."*i + "Q" + "."*(n-(i+1))

                            rows.append(s)

                            queen()

                            rows.pop()

                            column.remove(i)

                            right_diagonal.remove(i-len(rows))  # these lines need to write after removing from rows , becuase when i added this it was before adding in the rows

                            left_diagonal.remove(i+len(rows))

        queen()

        return result

    # this is BigO(N*N!) in Time and space is BigO(n^2)(n strings of n length)