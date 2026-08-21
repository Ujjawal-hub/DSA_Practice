# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):

        self.List = list()

    def inorder(self,root,low,high):

        if root == None:

            return

        self.inorder(root.left,low,high)

        if root.val >= low and root.val <= high:


            self.List.append(root.val)

        self.inorder(root.right,low,high)

        return

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.inorder(root,low,high)

        return sum(self.List)


# This is BigO(N) in Both space and Time


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root, low, high):

        total = 0

        if root == None:
            return 0

        if root.val >= low:
            total += self.inorder(root.left, low, high)

        if root.val >= low and root.val <= high:
            total += root.val

        if root.val <= high:
            total += self.inorder(root.right, low, high)

        return total

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        return self.inorder(root, low, high)

# This is BigO(N) in  Time  and BigO(h) in space