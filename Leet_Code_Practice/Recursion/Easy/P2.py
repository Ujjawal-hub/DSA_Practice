#Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        self.recursion(s, 0, len(s) - 1)

    def recursion(self, array, start, end):
        if start >= end:
            return

        array[start], array[end] = array[end], array[start]

        self.recursion(array, start + 1, end - 1)

        return

# this solution is BigO(N) in Time and space
# same swapping if done by iterative version then it would be O(1) space
# here we are practicing recrusion