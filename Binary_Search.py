def mid_point(left, right):
    half_length = int(((right + 1 - left) / 2) + 1)

    i = left - 1 + half_length

    return i

    # mid = (left + right) // 2

#Iterative version
def Binary_Search(array, target):
    right = len(array) - 1

    left = 0

    while right >= left:

        index = mid_point(left, right)

        value = array[index]

        if value == target:

            return "Found at index : " + str(index)



        elif value > target:

            right = index - 1

        elif value < target:

            left = index + 1

    return "Not found"

# Recursive Version
def Binary_Search_R(array, target):
    left = 0

    right = len(array) - 1

    return Binary_Search_R1(array, left, right, target)


def Binary_Search_R1(array, left, right, target):

    if left > right:
        return "Not found"

    index = mid_point(left, right)

    value = array[index]

    if value == target:

        return "Found value at : " + str(index)



    elif value > target:

        right = index - 1

        return Binary_Search_R1(array, left, right,
                                target)  # sending the a=same array again will not create extra space as it is just a reference

    elif value < target:

        left = index + 1

        return Binary_Search_R1(array, left, right, target)

# Iterative version:

# 	Complexity	      Reason
# Time	O(log n)	halves search space each iteration
# Space	O(1)	just a few variables, no extra memory

# Recursive version:

# 	Complexity	        Reason
# Time	O(log n)	same logic, halves each call
# Space	O(log n)	one stack frame per call, log n calls total