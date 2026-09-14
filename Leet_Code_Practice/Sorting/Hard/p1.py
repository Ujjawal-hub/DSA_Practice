#Given an integer array nums, return an integer array counts where counts[i]
# is the number of smaller elements to the right of nums[i].


class Solution:

    def __init__(self):

        self.dict = dict()

    def merge(self, left, right):

        li = 0
        ri = 0
        count = 0
        merged = list()

        while li < len(left) and ri < len(right):

            if left[li][0] <= right[ri][0]:

                merged.append(left[li])

                if left[li] not in self.dict:

                    self.dict[left[li]] = count

                else:

                    self.dict[left[li]] += count

                li += 1

            else:

                merged.append(right[ri])

                ri += 1

                count += 1

        if li == len(left):

            while ri < len(right):
                merged.append(right[ri])

                ri += 1

                count += 1

        elif ri == len(right):

            while li < len(left):

                merged.append(left[li])

                if left[li] not in self.dict:

                    self.dict[left[li]] = count

                else:

                    self.dict[left[li]] += count

                li += 1

        return merged

    def merge_sort(self, start, end, array):

        left_start = start

        left_end = start + (end - start) // 2

        right_start = left_end + 1

        right_end = end

        if start == end:
            return [array[start]]

        left = self.merge_sort(left_start, left_end, array)
        right = self.merge_sort(right_start, right_end, array)

        return self.merge(left, right)

    def countSmaller(self, nums: List[int]) -> List[int]:

        array = list()

        for i in range(0, len(nums)):
            array.append((nums[i], i))

        self.merge_sort(0, len(array) - 1, array)

        count = [0] * (len(array))

        for i in self.dict:
            no, index = i

            c = self.dict[i]

            count[index] = c

        return count

# this solution is BigO(nlogn) in Time and BigO(N) in space
#