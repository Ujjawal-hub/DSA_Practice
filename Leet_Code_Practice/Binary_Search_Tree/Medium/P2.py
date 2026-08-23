# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        if root != None:

            queue.append(root)

        length = len(queue)

        result = list()

        while queue:

            List = list()

            while length:

                p = queue.popleft()

                if p.left != None:

                    queue.append(p.left)

                if p.right != None:

                    queue.append(p.right)

                List.append(p.val)


                length -= 1

            length = len(queue)

            result.append(List)

        return result

# This is BigO(N)in Both space and Time