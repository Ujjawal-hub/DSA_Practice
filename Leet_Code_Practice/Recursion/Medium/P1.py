#Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.
#

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        if k == 1:

            List = list()

            for i in range(1, n + 1):
                List.append([i])

            return List

        if n == k:

            List = list()

            for i in range(1, n + 1):
                List.append(i)

            return [List]

        List1 = self.combine(n - 1, k)

        List2 = self.combine(n - 1, k - 1)

        for i in List2:
            i.append(n)

            List1.append(i)

        return List1
