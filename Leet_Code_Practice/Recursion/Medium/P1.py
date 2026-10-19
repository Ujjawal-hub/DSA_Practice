#Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.
#

# class Solution:
    # def combine(self, n: int, k: int) -> list[list[int]]:
    #
    #     if k == 1:
    #
    #         List = list()
    #
    #         for i in range(1, n + 1):
    #             List.append([i])
    #
    #         return List
    #
    #     if n == k:
    #
    #         List = list()
    #
    #         for i in range(1, n + 1):
    #             List.append(i)
    #
    #         return [List]
    #
    #     List1 = self.combine(n - 1, k)
    #
    #     List2 = self.combine(n - 1, k - 1)
    #
    #     for i in List2:
    #         i.append(n)
    #
    #         List1.append(i)
    #
    #     return List1

    class Solution:
        def combine(self, n: int, k: int) -> list[list[int]]:

            result = list()

            path = list()

            def backtraking(start):

                if len(path) == k:
                    result.append(path[:])

                    return

                for i in range(start, n + 1):
                    path.append(i)
                    backtraking(i + 1)
                    path.pop()

            backtraking(1)

            return result

        # this is BigO(C(n,k)*k) in Time C(n,k) is combitaions and multiply by k due to copying each list to result ,for space it is BigO(k) , k depth stack and also k memory for path