# #The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

class MedianFinder:

    def __init__(self):

        self.upper_half = list()
        self.lower_half = list()

    def addNum(self, num: int) -> None:

        heapq.heappush(self.upper_half, num)

        q = heapq.heappop(self.upper_half)

        heapq.heappush(self.lower_half, -q)

        if len(self.lower_half) > len(self.upper_half) + 1:
            l = heapq.heappop(self.lower_half)

            heapq.heappush(self.upper_half, -l)

    def findMedian(self) -> float:

        if len(self.upper_half) != len(self.lower_half):

            return -self.lower_half[0]

        else:

            return (-self.lower_half[0] + self.upper_half[0]) / 2


    #this BigO(logn) in Time and BigO(n) in space