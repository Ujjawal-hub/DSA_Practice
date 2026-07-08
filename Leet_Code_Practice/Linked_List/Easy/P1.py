#Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current != None:
            next1 = current.next
            current.next = prev
            prev = current
            current = next1

        head = prev

        return head

# this is time Big0(n) and bigO(1) space
