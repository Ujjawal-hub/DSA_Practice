class Queuea:

#Array implementation of Queue

    def __init__(self,value=None,capacity=10):

        self.capacity = capacity
        self._list1 = [None]*capacity
        self.frontindex = 0
        self._list1[0] = value
        if value != None:
            self.size = 1
        else:
            self.size = 0

    def enqueue(self,value):

        if self.size < self.capacity:

            end_index = (self.frontindex + self.size)%self.capacity
            self._list1[end_index] = value
            self.size += 1
        else:

            print("Sorry seats are full")

    # enqueue is BigO(1) in Time as it directly put the value at its place
    #without any shifting or iteration

    def dequeue(self):

        a = self._list1[self.frontindex]

        if self.size > 0:
            self._list1[self.frontindex] = None
            self.frontindex = (self.frontindex + 1)%self.capacity
            self.size -= 1
            return a

    #deletation operation does not shift any element so it is also BigO(1) in Time

    def empty(self):

        return self.size == 0


    def full(self):

        return self.size == self.capacity

    def __str__(self):

        return str(self._list1)