# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
#
# Implement the MyQueue class:
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
#
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
#
class MyQueue:

    def __init__(self):

        self.list1 = list()
        self.list2 = list()
        self.size = 0

    def push(self, x: int) -> None:

        while len(self.list2) != 0:
            self.list1.append(self.list2.pop())

        self.list1.append(x)

        self.size += 1

    # BigO(N) In Time and BigO(1) in Space

    def pop(self) -> int:

        while len(self.list1) != 0:
            self.list2.append(self.list1.pop())

        self.size -= 1

        return self.list2.pop()

#BigO(n) in Time and BigO(1) in space

    def peek(self) -> int:

        while len(self.list1) != 0:
            self.list2.append(self.list1.pop())

        return self.list2[-1]
#BigO(N) in Time and BigO(1) in space

    def empty(self) -> bool:

        return self.size == 0

#BigO(1) in Both space and Time

    # Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()