#Given the head of a linked list, remove the nth node from the
# end of the list and return its head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head,n):

        current = head

        length = 0

        while current != None:

            length += 1

            current  = current.next

        nlength = length - n

        current = head

        i = 1

        if nlength != 0:

            while i < nlength:

                current = current.next

                i += 1

            current.next = (current.next).next


            return head

        else:

            head = current.next

            return head

# This solution is BigO(n) in Time and BigO(1) in Space

# class Solution:
#
#     def reverse(self,head):
#
#
#         current = head
#         prev = None
#
#         while current != None:
#
#
#             next1 = current.next
#             current.next =prev
#             prev = current
#             current = next1
#
#         return prev
#
#     def removeNthFromEnd(self, head, n) :
#
#         head = self.reverse(head)
#
#         current = head
#
#         i = 1
#
#         if n>1:
#
#             while i < n-1:
#
#                 current = current.next
#
#                 i += 1
#
#             current.next = (current.next).next
#
#         else:
#
#             head = current.next
#
#         head = self.reverse(head)
#
#         return head

# This is the second Solution this is BigO(n) is Time and BigO(1) in space

# Follow up: Could you do this in one pass?

class Solution:
    def removeNthFromEnd(self, head, n):
        current = head

        list1 = list()

        length = 0

        while current != None:
            list1.append(current)

            current = current.next

            length += 1

        if n == length:
            head = head.next

        else:

            a = list1[length - n - 1]

            a.next = (a.next).next

        return head

#this solution is BigO(n) in time and BigO(n) in space as well  but this solution is done in single pass
