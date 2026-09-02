#Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]

    # this is BigO(nlogn) in Time and BigO(1) in space

    # this is standered solution

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Build a Min-Heap with the first K elements - O(K)
        min_heap = nums[:k]
        heapq.heapify(min_heap)

            # Process the remaining elements - O((N - K) log K)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

    #Time Complexity: BigO(Nlogk)
    #space complexity BiGO(k)