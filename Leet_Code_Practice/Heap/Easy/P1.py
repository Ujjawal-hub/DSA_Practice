#You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.


# class KthLargest:

    # def shift_down(self, index, last_index):
    #
    #     left = None
    #     right = None
    #     current = self.List[index]
    #
    #     if 2 * index + 1 <= last_index:
    #         left = self.List[2 * index + 1]
    #
    #     if 2 * index + 2 <= last_index:
    #         right = self.List[2 * index + 2]
    #
    #     if left == None:
    #         return
    #
    #     if right == None:
    #
    #         if current < left:
    #
    #             self.List[index], self.List[2 * index + 1] = left, current
    #
    #         else:
    #
    #             return
    #
    #     else:
    #
    #         if current > left and current > right:
    #
    #             return
    #
    #         else:
    #
    #             if left > right:
    #
    #                 self.List[index], self.List[2 * index + 1] = left, current
    #
    #                 self.shift_down(2 * index + 1, last_index)
    #
    #             else:
    #
    #                 self.List[index], self.List[2 * index + 2] = right, current
    #
    #                 self.shift_down(2 * index + 2, last_index)
    #
    #     return
    #
    # def heap_sort(self):
    #
    #     last_index = len(self.List) - 1
    #
    #     while last_index != 0:
    #         self.List[0], self.List[last_index] = self.List[last_index], self.List[0]
    #
    #         last_index -= 1
    #
    #         self.shift_down(0, last_index)
    #
    # def heap_build(self):
    #
    #     index = len(self.List) - 1
    #
    #     parent = (index - 1) // 2
    #
    #     while parent >= 0:
    #         self.shift_down(parent, index)
    #
    #         parent -= 1
    #
    # def __init__(self, k: int, nums: List[int]):
    #
    #     self.List = nums
    #     self.k = k
    #
    #     if len(nums) != 0:
    #
    #         self.heap_build()
    #
    #         self.heap_sort()
    #
    #         i = 1
    #
    #         h = list()
    #
    #         length = len(self.List)
    #
    #         while i <= length and i <= k:
    #             h.append(self.List.pop())
    #
    #             i += 1
    #
    #         self.List = h
    #
    # # this initialzation take BigO(nlogn) in Time and BigO(k+logn) in space
    #
    # def add(self, val: int) -> int:
    #
    #     if len(self.List) == 0 or (len(self.List) < self.k and val < self.List[-1]):
    #
    #         self.List.append(val)
    #
    #
    #
    #     elif val > self.List[-1]:
    #
    #         i = 0
    #
    #         while True:
    #
    #             if val > self.List[i]:
    #                 break
    #             i += 1
    #
    #         while i < len(self.List):
    #             temp = self.List[i]
    #
    #             self.List[i] = val
    #
    #             val = temp
    #
    #             i += 1
    #
    #         if len(self.List) < self.k:
    #             self.List.append(val)
    #
    #     return self.List[-1]
    #
    # # This add method is BigO(N) in Time and BigO(1) in space


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k

        self.nums = nums

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

    # BigO(nlogn) in Time and BigO(1) in space

    def add(self, val: int) -> int:

        if len(self.nums) < self.k:

            heapq.heappush(self.nums, val)


        elif val > self.nums[0]:

            heapq.heappushpop(self.nums, val)

        return self.nums[0]

        # this is BigO(logk) in  Time and BigO(1) in Space