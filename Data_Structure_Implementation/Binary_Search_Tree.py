class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_search_Tree:

    def __init__(self, value):

        self.root = Node(value)
        self.count = 1

    def insert(self, value):

        a = Node(value)

        b = self.root

        while True:

            if a.value > b.value:

                if b.right == None:

                    b.right = a

                    self.count += 1

                    break

                else:

                    b = b.right



            elif a.value < b.value:

                if b.left == None:

                    b.left = a

                    self.count += 1
                    break

                else:

                    b = b.left

        # BigO(h) in Time and BigO(1) in Space

    def inorder(self, root):

        if root == None:
            return

        self.inorder(root.left)

        print(root.value)

        self.inorder(root.right)

        return

        # This is BigO(N) in Time and BigO(h) in space

    def printTree(self):

        self.inorder(self.root)

    def is_in_tree(self, value):

        i = self.root

        while True:

            if i.value == value:

                return True

            elif i.value > value:

                i = i.left

            elif i.value < value:

                i = i.right

            if i == None:
                return False

    # BigO(h) in Time and BigO(1) in space

    def get_node_count(self):

        return self.count

    def delete_tree(self):

        self.root = None

    def height(self, root):

        if root == None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)

        # This is BigO(n) in Time and BigO(h) in space

    def get_height(self):

        return self.height(self.root)

    def get_min(self):

        i = self.root

        while True:

            if i.left == None:

                return i.value

            else:

                i = i.left

    # BigO(h) in Time and BigO(1) in space

    def get_max(self):

        i = self.root

        while True:

            if i.right == None:

                return i.value

            else:

                i = i.right

    def finding_element_parent(self, value):

        i = self.root

        parent = (None, None)

        while True:

            if i.value == value:

                break

            elif i.value < value:

                parent = (i, "right")

                i = i.right

            else:

                parent = (i, "left")

                i = i.left

        return parent

        # This is BigO(h) in Time AND BigO(1) in Time

    def find_element(self, value):

        parent, string = self.finding_element_parent(value)

        if string == "left":

            return parent.left

        elif string == "right":

            return parent.right

        else:

            return self.root

        # This is BigO(h) in Time AND BigO(1) in Time

    def successor_parent(self, value):

        i = self.find_element(value)

        parent = (None, None)

        if i.right != None:

            parent = (i, "right")

            i = i.right

            while i.left != None:
                parent = (i, "left")

                i = i.left

        return parent

        # This is BigO(h) in Time AND BigO(1) in Time

    def successor(self, value):

        parent, string = self.successor_parent(value)

        if string == "left":

            return parent.left

        elif string == "right":

            return parent.right

        else:

            return -1

            # This is BigO(h) in Time AND BigO(1) in Time

    def delete(self, value):

        i, string = self.find_element(value)

        p_i, p_string = self.find_element_parent(value)

        if i.left != None ^ i.right != None:  # ^ XOR operator means only one condition can be true

            child = None

            if i.left != None:

                child = i.left

            else:

                child = i.right

            if p_string == "left":

                p_i.left = child

            elif p_string == "right":

                p_i.right = child

            else:

                self.root = child

            self.count -= 1



        elif i.left == None and i.right == None:

            if p_string == "left":

                p_i.left = None

            elif p_string == "right":

                p_i.right = None

            else:

                self.root = None

            self.count -= 1





        else:

            successor = self.successor(value)

            self.delete(successor)

            successor.right = i.right
            successor.left = i.left

            if p_string == "left":

                p_i.left = successor

            elif p_string == "right":

                p_i.right = successor

            else:

                self.root = successor

            # here i will not write self.count -= 1 becuase that would be cover in the recurssion call , that above 2 of three case would definately run in this particular case

        # This is BigO(h) in Time AND BigO(1) in Time


tree = Binary_search_Tree(50)

tree.insert(40)
tree.insert(60)
tree.insert(30)
tree.insert(44)
tree.insert(55)
tree.insert(65)
tree.insert(20)
tree.insert(42)
tree.insert(46)
tree.insert(25)

tree.delete(50)
tree.printTree()







