# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


from collections import deque











class MinStack:

    def __init__(self):

        self.list1 = deque()
        self.min = None
        self.list2 = deque()

    def push(self, value: int) -> None:

        self.list1.append(value)

        if len(self.list2) != 0:

            if self.list2[-1] >= value:
                self.list2.append(value)

        else:

            self.list2.append(value)

# BigO(1) in both time and space

    def pop(self) -> None:

        a = self.list1.pop()

        if self.list2[-1] == a:
            self.list2.pop()

#BigO(1) in both time and space

    def top(self) -> int:

        return self.list1[-1]

#BigO(1) in both time and space

    def getMin(self) -> int:

        return self.list2[-1]

# BigO(1) in both time and space

# oveall this class is bigO(N) in both space and time