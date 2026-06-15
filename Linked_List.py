class Node:

    def __init__(self,value):

        self.value = value
        self.next = None

    def __str__(self):
        return f"value : {self.value} and next pointer address {self.next}"


class Linked_List:

    def __init__(self, head=None):

        self.head = head

        if (self.head != None):

            self.size = 1
        else:
            self.size = 0

    # this insert is BigO(n) but maintain insertion oder

    def pushback(self, node):

        if self.head != None:

            tmp = self.head

            while tmp.next != None:
                tmp = tmp.next

            tmp.next = node



        else:
            self.head = node

        self.size += 1

    # this fast_insert is BigO(1)  but insertion order is compromised

    def fast_insert(self, node):

        tmp = self.head
        self.head = node
        self.head.next = tmp

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

            return tmp
        else:
            return None

    def pop_back(self):

        tmp = self.head

        if self.head != None and self.size > 1:

            i = 1

            while i < self.size - 1:
                tmp = tmp.next

                i += 1

            tmp2 = tmp.next

            tmp.next = None

            self.size -= 1

            return tmp2

        else:

            if self.head != None:
                self.size -= 1

            self.head = None

            return tmp

    def front(self):

        return self.valueat(0)

    def back(self):

        return self.valueat(self.size - 1)

    def insert(self, index, node):

        tmp = self.head

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

            self.size -= 1

        elif index == 0 and self.head != None:

            self.head = self.head.next

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

        i = 0

        while i < self.size:
            tmp = self.pop_back()

            self.insert(i, tmp)

            i += 1

    def remove_value(self, node):

        self.pop_front()

        self.insert(0, node)





