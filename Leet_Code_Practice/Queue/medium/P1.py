# You are given an array of integers nums, there is a sliding window of
# size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window
# moves right by one position.
#
# Return the max sliding window.

from collections import deque

class Solution:

    def maxSlidingWindow(self, nums, k):

        window = deque()
        maxwindow = list()

        i = 1

        window.append(nums[0])

        while i < k:

            while len(window) != 0 and window[-1] < nums[i]:
                window.pop()

            window.append(nums[i])

            i += 1

        maxwindow.append(window[0])

        i = 0
        j = k

        while j < len(nums):

            if nums[i] == window[0]:
                window.popleft()

            while len(window) != 0 and window[-1] < nums[j]:
                window.pop()

            window.append(nums[j])

            maxwindow.append(window[0])

            i += 1
            j += 1

        return maxwindow

# this is 2n in time n for apending nfor deleting and k +n in space k space at any point and n for maxwindow array
# so this is BigO(N) in both space and time