# #You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#
#         heap = list()
#
#         length = len(lists)
#
#         i = 0
#
#         count = 0
#
#         while i < length:
#
#             nxtnode = lists[i]
#
#             while nxtnode and nxtnode != None:
#                 val = nxtnode.val
#
#                 heapq.heappush(heap, (val, count, nxtnode))
#
#                 nxtnode = nxtnode.next
#
#                 count += 1
#
#             i += 1
#
#         if len(heap) != 0:
#
#             val, count, current = heapq.heappop(heap)
#
#             head = current
#
#             i = 1
#
#             while heap:
#                 val, count, node = heapq.heappop(heap)
#
#                 current.next = node
#
#                 current = node
#
#             return head
#
#
#
#
#
#         else:
#
#             return None
#
# # this is BigO(nlongn) in Time and BigO(N) in Space

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = list()

        i = 0

        while i < len(lists):

            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

            i += 1

        if len(heap) != 0:

            val, count, current = heapq.heappop(heap)

            head = current

            while heap:

                if current.next != None:
                    heapq.heappush(heap, (current.next.val, i, current.next))

                val, count, node = heapq.heappop(heap)

                current.next = node

                current = node

                i += 1

            return head



        else:

            return None

        # this is BigO(nlogk) in time and BigO(k) in space   where k is number of linked list and n is total number of nodes