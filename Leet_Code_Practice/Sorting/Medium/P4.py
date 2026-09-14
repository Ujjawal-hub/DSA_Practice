#Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self, left, right):

        current1 = left

        current2 = right

        current = None

        if right == None or left.val <= right.val:

            head = current1

            current = head

            current1 = current1.next

        else:

            head = current2

            current = head

            current2 = current2.next

        while current1 != None or current2 != None:

            if (current1 != None and current2 != None) and current1.val <= current2.val:

                current.next = current1

                current1 = current1.next

            elif (current1 != None and current2 != None) and current1.val > current2.val:

                current.next = current2

                current2 = current2.next

            else:

                if current1 == None:

                    current.next = current2

                    current2 = current2.next

                elif current2 == None:

                    current.next = current1

                    current1 = current1.next

            current = current.next

        tail = current

        return (head, tail)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        length = 1
        prev = None
        last_element = None

        current = head

        while head != None and current.next != None:
            current = current.next

            length += 1

        list_length = 1

        while list_length < length:

            iteration = 0

            last = None

            current = head

            while current:

                left_head = None

                right_head = None

                for j in range(0, 2):

                    headlr = current

                    i = 1

                    while i <= list_length:

                        if current == None:
                            break

                        prev = current

                        current = current.next

                        i += 1

                    if j == 0:

                        left_head = headlr

                    elif j == 1:

                        right_head = headlr

                    prev.next = None

                start, end = self.merge(left_head, right_head)

                if last == None:

                    head = start

                else:

                    last.next = start

                last = end

            list_length = list_length * 2

        return head

# This solution is BigO(nlogn) in Time and BigO(1) in space 