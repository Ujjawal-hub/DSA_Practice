# [21,17,16,15,14,13,12,11,10,9,8]

class Heap:

    def __init__(self, value=None):

        self.size = 0

        if value != None:

            self.List = [value]

            self.size = 1

        else:

            self.List = []

    def shift_up(self, index):

        if index == 0:
            return

        parent_index = (index - 1) // 2

        current = self.List[index]
        parent = self.List[parent_index]

        if current > parent:
            self.List[index], self.List[parent_index] = self.List[parent_index], self.List[index]

            self.shift_up(parent_index)

        return

    # this is BigO(logn) in Both space and Time

    def insert(self, value):

        self.List.append(value)

        self.size += 1

        self.shift_up(self.size - 1)

    # this is BigO(logn) in Both space and Time

    def get_max(self):

        return self.List[0]

    def get_size(self):

        return self.size

    def is_empty(self):

        return self.size == 0

    def shift_down(self, index, array,
                   last_index=None):  # this last_index paramenter only written here to keep heap sort in mind so i can manipulate where shiftdown should stop

        current = array[index]

        if last_index == None:
            last_index = len(array) - 1

        left_child = None
        right_child = None

        if 2 * index + 1 <= last_index:
            left_child = array[2 * index + 1]

        if 2 * index + 2 <= last_index:
            right_child = array[2 * index + 2]

        if left_child == None:
            return

        if right_child == None:

            if current > left_child:

                return

            else:

                array[index], array[2 * index + 1] = left_child, current

                return

        else:

            if current > left_child and current > right_child:

                return

            else:

                if left_child > right_child:

                    array[index], array[2 * index + 1] = left_child, current

                    self.shift_down(2 * index + 1, array)

                else:

                    array[index], array[2 * index + 2] = right_child, current

                    self.shift_down(2 * index + 2, array)

        return

    # this will take BigO(logn) in Both space and Time

    def extract_max(self):

        self.List[0], self.List[self.size - 1] = self.List[self.size - 1], self.List[0]

        _max = self.List.pop()

        self.size -= 1

        self.shift_down(0, self.List)

        return _max

        # this will take BigO(logn) in Both space and Time

    def remove(self, x):

        self.List[x], self.List[self.size - 1] = self.List[self.size - 1], self.List[x]

        value = self.List.pop()

        self.size -= 1

        self.shift_down(x, self.List)

        return value

        # this will take BigO(logn) in Both space and Time

    def heap_build(self, array):

        child_index = len(array) - 1

        index = (child_index - 1) // 2

        while index >= 0:
            self.shift_down(index,
                            array)  # this shift down will not go recurcively below as below this index heap rules are already foloowed so it will run only one time

            index -= 1

        return array

    # heap_build will run BigO(n) Time abd BigO(1) in Space

    def heap_sort(self, array=None):

        if array != None:

            array = self.heap_build(array)

        else:

            array = self.List

        last_index = len(array) - 1

        while last_index != 0:
            array[0], array[last_index] = array[last_index], array[0]

            last_index -= 1

            self.shift_down(0, array, last_index)

        return array

# heap build take BiGO(n) time and one shift down take BigO(logn) in both space and Time so doing it n times
# this is BigO(nlogn) in Time and BigO(logn) in space


h = Heap(2)

h.insert(21)
h.insert(17)
h.insert(16)
h.insert(15)
h.insert(14)
h.insert(12)
h.insert(11)
h.insert(9)
h.insert(8)
h.insert(7)
h.insert(6)
h.insert(18)

h.remove(1)

print(h.List)

print(h.extract_max())
print(h.extract_max())
print(h.extract_max())
print(h.extract_max())
print(h.extract_max())
print(h.extract_max())
print(h.extract_max())
print(h.extract_max())
print(h.extract_max())
print(h.extract_max())
print(h.extract_max())


print(h.List)



print(h.get_size())