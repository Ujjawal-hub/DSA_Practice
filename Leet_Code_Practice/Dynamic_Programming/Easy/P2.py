#You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
#
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the staircase, which is the position just past the last step (index cost.length).
#

class Solution:
    def minCostClimbingStairs(self, cost: list[int], index=None, memo=None) -> int:

        if index == None and memo == None:
            index = len(cost)

            memo = dict()

        if index in memo:
            return memo[index]

        if index < 0:
            return 0

        child = min(self.minCostClimbingStairs(cost, index - 1, memo),
                    self.minCostClimbingStairs(cost, index - 2, memo))

        if index == len(cost):

            return child

        else:

            memo[index] = child + cost[index]

            return memo[index]

        # brute force is BigO(2^N)in Time and BigO(N) in space

# memo version is BigO(n) in Time and BigO(N) in space