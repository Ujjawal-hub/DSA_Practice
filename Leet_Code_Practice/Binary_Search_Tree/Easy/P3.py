#Given the roots of two binary trees p and q, write a function to check if they are the same or not.

#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def add(self, root, queue):

        if root == None:
            return

        if root.left != None:

            queue.append(root.left)

        else:

            queue.append(None)

        if root.right != None:

            queue.append(root.right)

        else:

            queue.append(None)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue1 = deque()
        queue2 = deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 or queue2:

            a = queue1.popleft()
            b = queue2.popleft()

            if a == None or b == None:

                if a != b:
                    return False

            elif a.val != b.val:

                return False

            self.add(a, queue1)

            self.add(b, queue2)

        return True

    # This is BigO(n) in Time and BigO(2^(h-1)) in Space
