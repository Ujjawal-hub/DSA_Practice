# #You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into
# on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.
#

class Solution:
    def rob(self, nums: list[int], index=None, memo=None) -> int:

        # if index == None and memo == None:

        #     index = len(nums)

        #     memo = dict()

        #     return max(self.rob(nums,index-1,memo),self.rob(nums,index-2,memo))

        # if index in memo:

        #     return memo[index]

        # if index < 0:

        #     return 0

        # memo[index] =  max(self.rob(nums,index-2,memo),self.rob(nums,index-3,memo)) + nums[index]

        # return memo[index]

        # brute force is BigO(2^N/2) in Time and BigO(n) in space

        # memoization is BigO(N) in Both space and time

        # tabulation approach

        # array = [0]*(len(nums)+1)

        # for i in range(0,len(nums)):

        #     robbed = array[i] + nums[i]

        #     next_h = i+2

        #     nex_next_h  = i+3

        #     if next_h >= len(array):

        #         next_h = -1

        #     if robbed > array[next_h]:

        #         array[next_h] = robbed

        #     if nex_next_h >= len(array):

        #         nex_next_h = -1

        #     if robbed > array[nex_next_h]:

        #         array[nex_next_h] = robbed

        # return array[-1]

        # tabulation approach is BigO(n) in time and BigO(N) in space

        # optimized tabulation

        house_1 = 0
        house_2 = 0
        house_3 = 0
        house_4 = 0

        for rob in nums:

            robbed = house_1 + rob

            if house_3 < robbed:
                house_3 = robbed

            if house_4 < robbed:
                house_4 = robbed

            house_1 = house_2
            house_2 = house_3
            house_3 = house_4
            house_4 = 0

        return max(house_1, house_2, house_3)

        # this is BigO(N) in time and BigO(1) in space


