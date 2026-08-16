from ..pre_requestie import treecreator

A = treecreator("ABCDEFGHI")


"""
Tree built from "ABCDEFGHI":

                       A
                     /   \
                    B     C
                   / \   / \
                  D   E F   G
                 / \
                H   I

A -> left: B, right: C
B -> left: D, right: E
C -> left: F, right: G
D -> left: H, right: I
E, F, G, I -> leaves (no children)
"""

def post_order(root):

    if root == None:

        return

    post_order(root.left)

    post_order(root.right)

    print(root.value)

    return

# BigO(N) in Time and BigO(logn) for balanced tree for space (logn base 2 = height ),for the worst case of space it will be BigO(N)