#Given the head of a singly linked list, return true
# if it is a palindrome or false otherwise.
#
from Linked_List import Node
from Linked_List import Linked_List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#
#         current = head
#
#         a = list()
#
#         while current != None:
#             a.append(current.val)
#
#             current = current.next
#
#         b = a[::-1]
#
#         if a == b:
#
#             return True
#
#         else:
#
#             return False
#
# #This solution is BigO(n) is Time and BigO(n) in space

class Solution:

    def reverse(self, node):

        current = node
        prev = None

        while current != None:
            next1 = current.next
            current.next = prev
            prev = current
            current = next1

        return prev

    def isPalindrome(self, head):

        current = head

        length = 0
        hlength = 1
        clength = 1

        node = None

        while current != None:
            length += 1

            current = current.next

        current = head

        while current != None:

            if length % 2 == 0:

                if hlength > length / 2:
                    node = self.reverse(current)

                    break



            else:

                if hlength > length / 2 + 1:
                    node = self.reverse(current)

                    break

            hlength += 1
            current = current.next

        current = head
        current1 = node

        while clength <= length / 2:

            if current.val == current1.val:

                pass
            else:

                return False

            current = current.next
            current1 = current1.next
            clength += 1

        return True

    #this solution is BigO(n) in Time and BigO(1) in space