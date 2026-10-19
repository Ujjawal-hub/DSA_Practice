#Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.

# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:
#
#         result = list()
#
#         sofar = list()
#
#         remaining = nums[:]
#
#         def permutation(sofar, remaining):
#
#             if len(sofar) == len(nums):
#                 result.append(sofar[:])
#
#                 return
#
#             for i in range(0, len(remaining)):
#                 sofar.append(remaining[i])
#
#                 remain = remaining[:i]
#
#                 remain.extend(remaining[i + 1:])  # extend returns NOne that is why i need to write this second line
#
#                 permutation(sofar, remain)
#
#                 sofar.pop()
#
#         permutation(sofar, remaining)
#
#         return result
#
#     # this is BigO(N*N!) in Time and space is BigO(N^2)

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = list()

        sofar = list()

        used = [False] * len(nums)

        def permutation():

            if len(sofar) == len(nums):
                result.append(sofar[:])

                return

            for i in range(0, len(nums)):

                if used[i] == True:
                    continue

                sofar.append(nums[i])

                used[i] = True

                permutation()

                sofar.pop()

                used[i] = False

        permutation()

        return result

    # this is BigO((N*N!) in Time and space is BigO(N)

    # For your permutation algorithm, the total number of nodes is the number of recursive calls across all levels of the recursion tree, including the root and the leaves.

# For your permutation algorithm, the total number of nodes is the number of recursive calls across all levels of the recursion tree, including the root and the leaves.

# For \(N\) input elements, the number of nodes at each level is:
# Level	Number of nodes
# 0	   1
# 1	   N
# 2	   N(N-1)
# 3	   N(N-1)(N-2)
#
# N	   N!
#
#
#
# So the exact total number of nodes is

#
#       1+N+N(N-1)+.........+N!

# The total number of nodes is \(O(N!)\), because the sum is bounded by a constant multiple of \(N!\).

# Since each node executes a loop with N iterations, your  # #   algorithm's time complexity is O(N*N!)  this is iteration only copying from so_far list to result is is also total time is N*N!