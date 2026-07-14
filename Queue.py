from Linked_List_t import Linked_List1
from  Linked_List import Node




# Linked List implementation of the queue

class Queue:

    def __init__(self, value=None):

        if value != None:
            a = Node(value)
        else:
            a = None

        self._b = Linked_List1(a)
        self.size = self._b.size

    def enqueue(self, value):
        tmp = Node(value)
        self._b.pushback(tmp)
        self.size = self._b.size

    # BigO(1) in Time as Linked use has info of tailpointer so pushback method used above is O(1)

    def dequeue(self):

        c = self._b.pop_front()
        self.size = self._b.size
        return c

    # BigO(1) in Time as removing from front of the linked list is BigO(1)
    def empty(self):

        return self._b.isempty()

    def __str__(self):

        return self._b.__str__()
        # return str(self.b)


