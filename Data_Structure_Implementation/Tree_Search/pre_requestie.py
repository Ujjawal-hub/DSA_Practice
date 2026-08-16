from collections import deque


class Node:

    def __init__(self,value):

        self.value = value
        self.left = None
        self.right = None

    def __str__(self):

        return str(self.value)


def treecreator(string):
    my_tree = Node(string[0])

    from collections import deque

    tracker = deque()

    tracker.append(my_tree)

    List = deque()

    for n in string[1::]:
        List.append(n)

    while List:

        N = tracker.popleft()

        a = Node(List.popleft())

        tracker.append(a)

        N.left = a

        if List:

            b = Node(List.popleft())

            tracker.append(b)

            N.right = b

        else:

            break

    return my_tree


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