#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # prev = None
        # current = head

        # while current != None:

        #     next1 = current.next
        #     current.next = prev
        #     prev = current
        #     current = next1

        # head = prev

        # return head

        if head != None:

            head,current = self.recursive_version(head,head)

        return head

    def recursive_version(self,current,head):

        if current.next == None:

            head = current

            return current,current

        head,current1 = self.recursive_version(current.next,head)

        current1.next = current

        current.next = None

        return head,current

    # this recursive version is BigO(n) in both space and time