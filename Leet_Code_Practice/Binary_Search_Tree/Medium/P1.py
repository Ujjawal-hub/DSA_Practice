# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):

        self.List = list()

    def inorder(self, root):

        if root == None:
            return

        self.inorder(root.left)

        self.List.append(root.val)

        self.inorder(root.right)

        return

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.inorder(root)

        i = 1

        while i != len(self.List):

            if self.List[i - 1] >= self.List[i]:
                return False

            i += 1

        return True

# This is BigO(N) in both time and space

