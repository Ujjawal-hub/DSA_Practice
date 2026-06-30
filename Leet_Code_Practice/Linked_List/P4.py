# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#
#         current = head
#
#         list1 = list()
#
#         while current != None:
#
#             if current in list1:
#
#                 return True
#
#             else:
#
#                 list1.append(current)
#
#             current = current.next
#
#         return False

    #this solution is BigO(n) in Time and BigO(n) in space as well

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head != None:
            current = head
            current2 = head

            while current != None:

                i = 0
                while i < 2:
                    if current2.next != None:
                        current2 = current2.next
                        i += 1

                    else:

                        return False

                current = current.next

                if current == current2:
                    return True

        else:
            return False
# this solution is BigO(n) in Time and in space BigO(1)




