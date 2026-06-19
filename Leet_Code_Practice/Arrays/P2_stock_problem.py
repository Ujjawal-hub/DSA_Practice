class Solution:

    #You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

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




