#Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#
#         freqdict = dict()
#
#         for i in nums:
#
#             if i in freqdict:
#
#                 freqdict[i] += 1
#
#             else:
#
#                 freqdict[i] = 1
#
#         count = dict()
#
#         for i in freqdict:
#
#             if freqdict[i] in count:
#
#                 count[freqdict[i]].append(i)
#
#             else:
#
#                 count[freqdict[i]] = [i]
#
#         freq = list()
#
#         for i in count:
#             freq.append(i)
#
#         List = freq[:k]
#
#         heapq.heapify(List)
#
#         for i in freq[k:]:
#
#             if i > List[0]:
#                 heapq.heappushpop(List, i)
#
#         for i in range(0, len(List)):
#             List[i] = -List[i]
#
#         heapq.heapify(List)
#
#         answer = list()
#
#         for i in range(0, len(List)):
#
#             j = heapq.heappop(List)
#
#             answer.extend(count[-j])
#
#             if len(answer) == k:
#                 break
#
#         return answer

# this is BigO(Nlogk) in Time and BigO(n) in space

#this is one in less code does same thing

class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequency of each number
    # Example: nums = [1, 1, 1, 2, 2, 3] -> count = {1: 3, 2: 2, 3: 1}
    count = Counter(nums)

    # Step 2: Initialize an empty list to act as our min-heap
    hp = []

    # Step 3: Iterate through every unique number and its frequency
    for num, freq in count.items():

      # Push (frequency, number) tuple into the heap.
      # Placing 'freq' first ensures the heap orders elements BY FREQUENCY.
      heapq.heappush(hp, (freq, num))

      # Step 4: Keep heap size strictly <= k.
      # If heap size reaches k + 1, remove the SMALLEST frequency element.
      if len(hp) > k:
        heapq.heappop(hp)

    # Step 5: Extract just the numbers from the remaining tuples in the heap.
    # The heap now contains the 'k' elements with the highest frequencies!
    return [num for freq, num in hp]

  #______________________________________________________________________
  #_____________________________________________________________________

  # this is code below does same thing in even less code

  class Solution:

      def topKFrequent(self, nums: list[int], k: int) -> list[int]:
          # Step 1: Count the frequency of every number in 'nums'.
          # Counter(nums) creates a dictionary mapping: number -> frequency.
          # Example: [1, 1, 1, 2, 2, 3] becomes {1: 3, 2: 2, 3: 1}
          counts = Counter(nums)

          # Step 2: Use 'heapq.nlargest' to find and return the 'k' most frequent elements.
          #
          # How each argument works:
          # 1. 'k': Specifies how many top elements we want to return.
          #
          # 2. 'counts.keys()': Supplies the list of unique numbers to evaluate (e.g., [1, 2, 3]).
          #
          # 3. 'key=counts.get': Tells heapq how to rank the unique numbers.
          #    Instead of comparing the numbers directly (e.g., 3 vs 1),
          #    heapq executes 'counts.get(num)' to extract and compare their frequencies
          #    (e.g., comparing frequency 3 vs frequency 1).
          #
          # Under the hood, heapq maintains a Min-Heap of size 'k' while scanning all unique keys,
          # leaving us with the 'k' elements that have the highest frequencies.
          return heapq.nlargest(k, counts.keys(), key=counts.get)
