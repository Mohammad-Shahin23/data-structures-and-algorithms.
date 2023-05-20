class Tree_Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree1:
    def __init__(self):
        self.root = None

    def pre_order(self, root):
        if root is not None:
            pre_list.append(root.value)
        if root.left is not None:
            self.pre_order(root.left)
        if root.right is not None:
            self.pre_order(root.right)

    def in_order(self, root):
        if root.left is not None:
            self.in_order(root.left)
        if root is not None:
             in_list.append(root.value)
        if root.right is not None:
            self.in_order(root.right)

    def post_order(self, root):
        """
        Perform post-order traversal on the tree rooted at the given node.
        """
        if root.left is not None:
            self.post_order(root.left)
        if root.right is not None:
            self.post_order(root.right) 
        if root is not None:
            post_list.append(root.value)

class BTS(Tree1):
    def __init__(self, value):
        """
        Initialize a BTS (Binary Search Tree) object with the given value.

        """
        super().__init__()
        self.value = value
        self.left = None
        self.right = None

    def add(self, num):
        """
        Add a node with the given value to the BTS.

        """
        if self.value is None:
            self.value = num
        elif num <= self.value:
            if self.left is None:
                self.left = Tree_Node(num)
            else:
                self.left.add(num)
        else:
            if self.right is None:
                self.right = Tree_Node(num)
            else:
                self.right.add(num)

    def contains(self, value):
        """
        Check if the BTS contains a node with the given value.


        Returns: A boolean indicating whether or not the value is present in the BTS.

        """
        if self.value == value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    



    


pre_list= []
in_list= []
post_list= []
BTS_list= []



print(newBTS.contains(50))
print(newBTS.right.value)
# expected_result = [5, 3, 2, 4, 7, 6, 8]
# assert(tree.pre_order(), expected_result)



# tree1 = Tree1()

# node1 = Tree_Node("A")
# tree1.root = node1

# node2 = Tree_Node("B")
# tree1.root.left = node2

# node3 = Tree_Node("C")
# tree1.root.right = node3

# node4 = Tree_Node("D")
# tree1.root.left.left = node4

# node5 = Tree_Node("E")
# tree1.root.left.right = node5

# node6 = Tree_Node("F")
# tree1.root.right.left = node6

# tree1.pre_order(tree1.root)
# print(pre_list)
# tree1.in_order(tree1.root)
# print(in_list)
# tree1.post_order(tree1.root)
# print(post_list)



# node1 = Tree_Node(50)
# newBTS.root = node1

# node2 = Tree_Node(40)
# newBTS.root.left = node2

# node3 = Tree_Node(60)
# newBTS.root.right = node3

# node4 = Tree_Node(65)
# newBTS.root.left.left = node4

# node5 = Tree_Node(45)
# newBTS.root.left.right = node5

# node6 = Tree_Node(30)
# newBTS.root.right.left = node6

# newBTS.add(newBTS.root,55)

# newBTS.pre_order(newBTS.root)
# print(pre_list)
# newBTS.in_order(newBTS.root)
# print(in_list)
# newBTS.post_order(newBTS.root)
# print(post_list)

# newBTS.in_order(newBTS.root)

