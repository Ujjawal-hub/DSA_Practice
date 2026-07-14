# This linked list implementaion has information of tail pointer also

class Linked_List1:

    def __init__(self, head=None):

        self.head = head
        self.tail = head

        if (self.head != None):

            self.size = 1
        else:
            self.size = 0

    # this insert is BigO(1) due to info of tailpointer maintain insertion oder


def pushback(self, node):
    if self.tail != None:

        self.tail.next = node

        self.tail = node



    else:
        self.head = node
        self.tail = node

    self.size += 1

    # this fast_insert is BigO(1)  but insertion order is compromised


def fast_insert(self, node):
    tmp = self.head
    self.head = node
    self.head.next = tmp

    if self.tail == None:
        self.tail = node

    self.size += 1

    # in this method i used list which is kind of a dynamic array using it kills
    # the purpose of using linked list ,but it used only for observation purpose


def __str__(self):
    tmp = self.head

    a = list()

    while tmp != None:
        a.append(tmp.value)

        tmp = tmp.next

    return str(a)

    #  def size(self):

    #     size = 0

    #        tmp = self.head

    #       while tmp != None:

    #          size += 1

    #         tmp = tmp.next

    #    return size


def isempty(self):
    return self.size == 0


def valueat(self, index):
    if index < self.size:

        tmp = self.head

        i = 1

        while i <= index:
            tmp = tmp.next

            i += 1

        return tmp.value

    else:

        raise IndexError("Stupid")


def pop_front(self):
    if self.head != None:

        tmp = self.head
        self.head = self.head.next

        self.size -= 1

        if self.size == 0:
            self.tail = None

        return tmp
    else:
        return None


def pop_back(self):
    tmp = self.head

    if self.size > 1:

        i = 1

        while i < self.size - 1:
            tmp = tmp.next

            i += 1

        tmp2 = tmp.next

        tmp.next = None

        self.tail = tmp

        self.size -= 1

        return tmp2

    else:

        if self.head != None:
            self.size -= 1

        self.head = None
        self.tail = None

        return tmp


def front(self):
    return self.valueat(0)


def back(self):
    return self.tail.value


def insert(self, index, node):
    tmp = self.head

    if index == self.size:
        self.tail = node

    if index <= self.size and index > 0:

        i = 1

        while i < index:
            tmp = tmp.next

            i += 1

        node.next = tmp.next

        tmp.next = node

        self.size += 1

    elif index == 0:

        self.head = node
        node.next = tmp

        self.size += 1

    else:
        raise IndexError("no no no try again")


def erase(self, index):
    tmp = self.head

    if index > 0 and index < self.size:

        i = 1

        while i < index:
            tmp = tmp.next

            i += 1

        tmp1 = (tmp.next).next
        tmp.next = tmp1

        if index == self.size - 1:
            self.tail = tmp

        self.size -= 1

    elif index == 0 and self.head != None:

        self.head = self.head.next

        if self.size == 1:
            self.tail = None

        self.size -= 1

    else:
        raise IndexError("invalid index")


def vlaue_n_from_end(self, n):
    if n <= self.size and n > 0:

        i = self.size - n

        return self.valueat(i)

    else:
        raise IndexError("stay inside the list")


def reverse(self):
    # this implementation in the comment is easy to code but it is bigO(n^2)

    # i = 0

    #   while i < self.size:

    #    tmp = self.pop_back()

    #      self.insert(i,tmp)

    #     i += 1

    # -----------------------------------

    # this implementation is BigO(n)

    i = 0

    current = self.head
    prev = None

    self.tail = self.head

    while i < self.size:
        next1 = current.next
        current.next = prev
        prev = current
        current = next1

        i += 1

    self.head = prev


def remove_value(self, value):
    i = 0

    while i < self.size:

        if value == self.valueat(i):
            self.erase(i)

            break
        i += 1
