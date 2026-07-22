# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
#
# Implement the MyStack class:
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
#
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

#Follow-up: Can you implement the stack using only one queue?


# here i am asumming list as a queue so any pop method will be treated as O(1) rather than O(n) which is the actual case for the list

class MyStack:

    def __init__(self):

        self.list1 = list()
        self.size = 0

    def push(self, x: int) -> None:

        self.list1.append(x)
        self.size += 1
# this BigO(1) both space and Time
    def pop(self) -> int:

        i = 1

        while i < self.size:
            self.list1.append(self.list1.pop(0))

            i += 1

        a = self.list1.pop(0)

        self.size -= 1

        return a

    # this is BigO(N) in Time and BigO(1) in space

    def top(self) -> int:

        i = 1

        while i < self.size:
            self.list1.append(self.list1.pop(0))

            i += 1

        a = self.list1[0]

        self.list1.append(self.list1.pop(0))

        return a

    # This is BigO(n) in Time and BigO(1) in space

    def empty(self) -> bool:

        return self.size == 0