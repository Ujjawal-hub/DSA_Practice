#We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
#
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
#
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def mid_point(self,left,right):

        return left + (right-left)//2

    def guessNumber(self, n: int) -> int:

        left = 1

        right = n

        while True:

            value = self.mid_point(left,right)

            result = guess(value)

            if 0 == result:

                return value

            elif -1 == result:

                right = value -1

            elif 1 == result:

                left = value +1

# This is BigO(logN) in Time and BigO(1) in sapce