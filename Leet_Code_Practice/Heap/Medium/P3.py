#Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
#

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        answer = list()

        for x, y in points:

            j = (x ** 2 + y ** 2) ** 0.5

            heapq.heappush(answer, (-j, (x, y)))

            if len(answer) > k:
                heapq.heappop(answer)

        return [i for h, i in answer]

    # this is BigO(nlogk) in Time and BigO(k) in space

#even in less code same thing

class Solution:

  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    # nsmallest keeps a max-heap of size k under the hood
    return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)