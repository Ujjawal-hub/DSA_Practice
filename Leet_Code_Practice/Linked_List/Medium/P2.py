#You are given the head of a singly linked-list. The list can be represented as:

#L0 → L1 → … → Ln - 1 → Ln
#Reorder the list to be on the following form:

#L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """

        length = 0

        current = head

        list1 = list()

        while current != None:
            list1.append(current)

            current = current.next

            length += 1

            i = 0
            j = 0

        while i + 1 < length / 2:
            j = length - 1 - i

            list1[i].next = list1[j]

            list1[j].next = list1[i + 1]

            i += 1

        if length > 2:
            list1[j - 1].next = None

#This solution is BigO(N) in TIME and BigO(n) in space as well
