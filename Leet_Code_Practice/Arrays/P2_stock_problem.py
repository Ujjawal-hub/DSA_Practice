class Solution:

    # this implementation is bigO(n^2)

    # def maxProfit(self, prices):
    #
    #     maxprofit = 0
    #
    #     i = len(prices) - 1
    #
    #     while i >= 0:
    #
    #         j = i - 1
    #
    #         while j >= 0:
    #
    #             new = prices[i] - prices[j]
    #
    #             if new > maxprofit:
    #                 maxprofit = new
    #
    #             j -= 1
    #
    #         i -= 1
    #
    #     return maxprofit

    def maxProfit(self, prices):

        maxprofit = 0

        potentialminvalue = prices[0]

        for i in prices:

            if i < potentialminvalue:
                potentialminvalue = i

            potentialprofit = i - potentialminvalue

            if potentialprofit > maxprofit:
                maxprofit = potentialprofit

        return maxprofit

    # time bigO(n)  space bigO(1)




