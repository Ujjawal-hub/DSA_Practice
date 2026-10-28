#You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#

class Solution:
    def climbStairs(self, n: int, memo=dict()) -> int:
        #     # memoize method

        #     if n == 0:

        #         return 1

        #     if n<0:

        #         return 0

        #     if n in memo:

        #         return memo[n]

        #     memo[n] = self.climbStairs(n-1,memo) + self.climbStairs(n-2,memo)

        #     return memo[n]

        # # memoize time is BigO(N) and space is O(N)

        # # brute force time O(2^N) and space O(N)

        # tabulation method

        # table = [0]*(n+1)

        # table[0] = 1

        # for i in range(0,len(table)):

        #     if table[i] != 0:

        #         if i+1 < len(table):

        #             table[i+1] += table[i]

        #         if i+2 <len(table):

        #             table[i+2] += table[i]

        # return table[n]

        # this tabulation method is BigO(n) in Time and O(N) in space

        # optimized tabulation solution

        current = 1
        next_one = 0
        next_two = 0

        for i in range(0, n):
            next_one += current
            next_two += current

            current = next_one
            next_one = next_two
            next_two = 0

        return current

    # this tabulation method is BigO(n) in Time and O(1) in space