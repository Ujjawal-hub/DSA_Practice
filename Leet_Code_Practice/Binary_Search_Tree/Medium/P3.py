# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def shifting(self, root, node):

        if root.val == node.val:

            return None

        elif root.val < node.val:

            root = root.right

        else:

            root = root.left

        return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        root1 = root

        root2 = root

        while root1 == root2:
            root = root1

            root1 = self.shifting(root, p)

            root2 = self.shifting(root, q)

        return root


# this is BigO(h) in time and BigO(1) in space