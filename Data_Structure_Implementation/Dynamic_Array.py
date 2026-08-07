class Dynamic_Array:

    def __init__(self):

        self.array = [None]
        self.capacity = 1
        self.size = 0

    def push(self, num):
        if (self.capacity == self.size):
            temp = [None] * 2 * self.size

            for i in range(0, self.size):
                temp[i] = self.array[i]

            self.array = temp
            self.capacity = 2 * self.size

        self.array[self.size] = num
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        return str(self.array)

    def at(self, index):
        if index < self.size:
            return self.array[index]
        else:
            raise IndexError("out of bounds")

    def insert(self, index, item):

        if index >= self.size:
            raise IndexError("out of bounds")

        else:
            for i in range(index, self.size):
                temp1 = self.array[i]

                self.array[i] = item

                item = temp1

            self.push(item)

    def is_empty(self):

        return self.size == 0

    def prepend(self, item):

        self.insert(0, item)

    def pop(self):

        temp = self.array[self.size - 1]
        self.delete(self.size - 1)

        return temp

    def delete(self, index):

        if index < self.size:

            for i in range(index + 1, self.size):
                self.array[i - 1] = self.array[i]

            self.array[self.size - 1] = None

            self.size -= 1

            self.resize()

    def remove(self, item):

        for i in range(0, self.size):

            if self.array[i] == item:
                self.delete(i)

    def find(self, item):

        for i in range(0, self.size):

            if self.array[i] == item:
                return i

        else:
            return -1

    def resize(self):

        if self.size <= 0.25 * (self.capacity):

            temp = [None] * int(self.capacity * 0.5)

            for i in range(0, self.size):
                temp[i] = self.array[i]

            self.array = temp

            self.capacity = int(0.5 * self.capacity)








