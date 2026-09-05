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


    #Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    #below two are standerd solutions for the follow up

class BoundedMedianFinder:

    def __init__(self):
        self.counts = [0] * 101  # Direct indexing for values 0 through 100
        self.total_count = 0

    def addNum(self, num: int) -> None:
          self.counts[num] += 1
          self.total_count += 1

    def findMedian(self) -> float:          # Target 1-based ranks for the middle element(s)
        target1 = (self.total_count + 1) // 2
        target2 = (self.total_count // 2) + 1

        count_so_far = 0
        val1, val2 = None, None

            # Linear scan across at most 101 buckets: O(1) time
        for val in range(101):
            count_so_far += self.counts[val]

            if val1 is None and count_so_far >= target1:
                val1 = val
            if val2 is None and count_so_far >= target2:
                val2 = val
                break

        if self.total_count % 2 != 0:
            return float(val1)
        return (val1 + val2) / 2.0


class SparseBoundedMedianFinder:

  def __init__(self):
    self.counts = [0] * 101  # Frequency buckets for 99% of values
    self.below = []  # Max-heap for outliers < 0 (negated values)
    self.above = []  # Min-heap for outliers > 100
    self.total_count = 0

  def addNum(self, num: int) -> None:
    if num < 0:
      heapq.heappush(self.below, -num)
    elif num > 100:
      heapq.heappush(self.above, num)
    else:
      self.counts[num] += 1
    self.total_count += 1

  def findMedian(self) -> float:
    target1 = (self.total_count + 1) // 2
    target2 = (self.total_count // 2) + 1

    def get_val_at_rank(rank: int) -> int:
      # 1. Rank falls in 'below' heap (< 0)
      if rank <= len(self.below):
        # Extract k-th element from max-heap without mutation
        sorted_below = sorted([-x for x in self.below])
        return sorted_below[rank - 1]

      # 2. Rank falls in [0, 100] bucket range
      current_rank = len(self.below)
      for val in range(101):
        current_rank += self.counts[val]
        if current_rank >= rank:
          return val

      # 3. Rank falls in 'above' heap (> 100)
      above_rank = rank - current_rank
      sorted_above = sorted(self.above)
      return sorted_above[above_rank - 1]

    val1 = get_val_at_rank(target1)
    if self.total_count % 2 != 0:
      return float(val1)

    val2 = get_val_at_rank(target2)
    return (val1 + val2) / 2.0



