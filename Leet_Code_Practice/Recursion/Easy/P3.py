#The Fibonacci numbers, commonly denoted F(n) form a sequence, called
# the Fibonacci sequence, such that each number is the sum of the two
# preceding ones, starting from 0 and 1. That is,

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:

            return 0

        if n == 1:

            return 1

        return self.fib(n-1) + self.fib(n-2)


    #   # this solution is BigO(2^N) in Time and max height of recursive depth is N  so space is BigO(N)   