# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
#
# Implement the RecentCounter class:
#
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


from collections import deque


# class RecentCounter:
#
#     def __init__(self):
#
#         self.list1 = list()
#
#     def ping(self, t: int) -> int:
#
#         self.list1.append(t)
#
#         h = t - 3000
#
#         f = len(self.list1)
#
#         index = f - 1
#
#         count = 0
#
#         while index >= 0:
#
#             if self.list1[index] >= h and self.list1[index] <= t:
#
#                 count += 1
#
#             else:
#
#                 break
#
#             index -= 1
#
#         return count
#
# # Your RecentCounter object will be instantiated and called as such:
# # obj = RecentCounter()
# # param_1 = obj.ping(t)

# below code is how it should be handeld ,sing queue , real world scenario

class RecentCounter:

    def __init__(self):
        self.list1 = deque()
        self.size = 0

    def ping(self, t):
        self.list1.append(t)

        self.size += 1

        h = t - 3000

        while self.list1[0] < h:
            self.list1.popleft()

            self.size -= 1

        return self.size