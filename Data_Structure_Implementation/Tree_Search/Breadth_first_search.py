from pre_requestie import treecreator,deque

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

def breadth_first_search(root):

    tracker = deque()

    tracker.append(root)

    while tracker:

        s = tracker.popleft()

        print(s)

        if s.left != None:

            tracker.append(s.left)

        if s.right != None:

            tracker.append(s.right)

# BigO(N) in Time and BigO(N/2) in space which is BigO(N) and for best space BigO(1)
# in balanced tree due to geomatric series last layer will contain aprrox n/2 element