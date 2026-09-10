from Linked_List import Linked_List1
from Linked_List import Node

import random


class Sorting:

    def merge_array(self, left, right):

        i = 0

        j = 0

        sort = list()

        while i < len(left) and j < len(right):

            if  (left[i] <= right[j]):  # this equal sign here for array1 which will be the left arrray ensure stablity of the merge sort

                sort.append(left[i])

                i += 1

            elif (left[i] > right[j]):

                sort.append(right[j])

                j += 1

        if i == len(left):

            while j < len(right):
                sort.append(right[j])

                j += 1

        elif j == len(right):

            while i < len(left):
                sort.append(left[i])

                i += 1

        return sort

    def merge_sort(self, data):

        if isinstance(data, list) and len(data) != 0:
            return self.merge_sort_array(data, 0, len(data) - 1)

        if isinstance(data, Node):

            current = data

            i = 1

            while current != None:
                current = current.next

                i += 1

            length = i - 1

            return self.merge_sort_linked_list(data, length)

    def merge_sort_array(self, array, start, end):

        left_end = start + (end - start) // 2
        left_start = start

        right_start = left_end + 1

        right_end = end

        if start == end:
            return [array[start]]

        left = self.merge_sort_array(array, left_start, left_end)
        right = self.merge_sort_array(array, right_start, right_end)

        return self.merge_array(left, right)

    # This is BigO(Nlogn) in Time and BigO(N) in space(logn recursion depth while also holding n elemnts in serate list n> logn)
    # merge sort is not in place algorithm,  merge sort is stable sorting
    def merge_linked_list(self, left, right):

        current1 = left

        current2 = right

        if left.value <= right.value:

            head = current1

            current1 = current1.next

        else:

            head = current2

            current2 = current2.next

        current = head

        while current1 != None and current2 != None:

            if current1.value <= current2.value:

                current.next = current1

                current1 = current1.next

            else:

                current.next = current2

                current2 = current2.next

            current = current.next

        if current1 != None:

            current.next = current1

        elif current2 != None:

            current.next = current2

        return head

    def merge_sort_linked_list(self, head, length):

        current = head

        left_length = length // 2
        right_length = length - left_length

        i = 1

        while i != left_length and left_length != 0:
            current = current.next

            i += 1

        head2 = current.next

        current.next = None

        if length == 1:
            return head

        left = self.merge_sort_linked_list(head, left_length)
        right = self.merge_sort_linked_list(head2, right_length)

        return self.merge_linked_list(left, right)

    # this is BigO(nlogn) in Time and BigO(logn) in space(recursion depth)

    def quicksort2way(self, array, start, end):

        index = random.randint(start, end)

        pivot = array[index]

        array[index], array[end] = array[end], array[index]

        lp = start
        rp = end - 1

        while lp < rp:

            if array[lp] <= pivot:
                lp += 1

            if array[rp] > pivot:
                rp -= 1

            if array[lp] > pivot:
                array[lp], array[rp] = array[rp], array[lp]

                rp -= 1

        if rp >= 0 and array[rp] > pivot:

            array[rp], array[end] = array[end], array[rp]

            index = rp

        else:

            array[rp + 1], array[end] = array[end], array[rp + 1]

            index = rp + 1

        if start < index - 1:
            self.quicksort2way(array, start, index - 1)

        if index + 1 < end:
            self.quicksort2way(array, index + 1, end)

        return

    # this is BigO(N^2) in Time and BigO(N) recussion depth space ,on average it is BigO(nlogn) in Time and BigO(longn) in space recusion space
    # quicksort is inplace algorithm , quicksort is not stable
    def quicksort3way(self, array, start, end):

        index = random.randint(start, end)

        array[start], array[index] = array[index], array[start]

        pivot = start

        lp = pivot + 1

        rp = end

        while lp <= rp:

            if array[lp] > array[pivot]:

                array[lp], array[rp] = array[rp], array[lp]

                rp -= 1

            elif array[lp] == array[pivot]:

                lp += 1

            elif array[lp] < array[pivot]:

                array[lp], array[pivot] = array[pivot], array[lp]

                lp += 1
                pivot += 1

        if pivot - 1 > start:
            self.quicksort3way(array, start, pivot - 1)

        if lp < end:
            self.quicksort3way(array, lp, end)

        # this is BigO(N^2) in Time and BigO(N) recussion depth space ,on average it is BigO(nlogn) in Time and BigO(longn) in space recusion space

    def insertion_sort(self, array):

        i = 1

        while i < len(array):

            if array[i] >= array[i - 1]:

                i += 1

            else:

                j = i

                while j >= 1 and array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]

                    j -= 1

                i += 1

        # this is BigO(n^2) in Time and BigO(1) in space and stable sorting and inplace sorting

    def selection_sort(self, array):

        sorted_index = 0

        while sorted_index < len(array):

            i = sorted_index
            min_index = i

            while i < len(array):

                if array[i] < array[min_index]:
                    min_index = i

                i += 1

            array[sorted_index], array[min_index] = array[min_index], array[sorted_index]

            sorted_index += 1

        # this is BigO(N^2) in Time and BigO(1) in space and it is not stable , and it is inplace sorting

        # heap sort is inplace and BigO(nlogn) in Time and BigO(1) in space ,but not stable