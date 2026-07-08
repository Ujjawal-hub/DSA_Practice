#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#
#         if list1.val <= list2.val:
#
#             list3 = list1
#             current = list1
#             currents = list2
#
#
#         else:
#             list3 = list2
#             current = list2
#             currents = list1
#
#         while True:
#
#             if current.next != None:
#
#                 if currents.val < current.next.val:
#
#                     tmp = current.next
#                     current.next = currents
#                     current = currents
#                     current.next = tmp
#
#                     if currents.next != None:
#
#                         currents = currents.next
#                     else:
#
#                         break
#
#                 else:
#
#                     if current.next != None:
#                         current = current.next
#
#             else:
#
#                 current.next = currents
#
#                 break
#
#         return list3

#The core issue is in this block:
# python
# tmp = current.next
# current.next = currents
# current = currents
# current.next = tmp
#
# if currents.next != None:
#     currents = currents.next
# After current = currents, current and currents are
# literally the same object. So when you do
# current.next = tmp, you're also setting currents.next = tmp —
# they're aliased. Then immediately after, you check
# currents.next to decide where to advance currents next...
# but you just overwrote that value with tmp! tmp belongs
# to the primary list (current's original chain), not the next node
# of the secondary list you're merging in. So
# currents = currents.next actually
# grabs tmp — a node already in the merged chain — instead
# of advancing to the real next node of the other list.

class Solution:
    def mergeTwoLists(self, list1, list2):

        if list1 != None and list2 != None:

            if list1.val <= list2.val:

                list3 = list1
                current = list1
                currents = list2


            else:
                list3 = list2
                current = list2
                currents = list1

            while True:

                if current.next != None:

                    if currents.val < current.next.val:

                        tmp = current.next
                        current.next = currents

                        if currents.next != None:

                            tmp1 = currents.next
                            currents.next = tmp
                            currents = tmp1
                        else:
                            currents.next = tmp
                            break

                    else:

                        if current.next != None:
                            current = current.next

                else:

                    current.next = currents

                    break

            return list3

        elif list1 == None:

            return list2

        else:

            return list1

# this is Time : Big0(n) and Space : BigO(1)
