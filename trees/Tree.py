class Tree_Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree1:
    def __init__(self):
        self.root = None

    def pre_order(self):
        arr=[]
        return self._pre_order(self.root, arr)
        


    def _pre_order(self, root, pre_list):
        if self.root is None:
            return pre_list
        
        if root is not None:
            pre_list.append(root.value)
        if root.left is not None:
            self._pre_order(root.left, pre_list)
        if root.right is not None:
            self._pre_order(root.right, pre_list)
        return pre_list

    def in_order(self):
        arr=[]
        return self._in_order(self.root, arr)
    
    def _in_order(self, root, in_list):
        if self.root is None:
            return in_list
        if root.left is not None:
            self._in_order(root.left, in_list)
        if root is not None:
             in_list.append(root.value)
        if root.right is not None:
            self._in_order(root.right, in_list)
        return in_list
    
    def post_order(self):
        arr=[]
        return self._post_order(self.root, arr)
    
    def _post_order(self, root, post_list= []):

        if self.root is None:
            return post_list
        """
        Perform post-order traversal on the tree rooted at the given node.
        """
        if root.left is not None:
            self._post_order(root.left, post_list)
        if root.right is not None:
            self._post_order(root.right, post_list) 
        if root is not None:
            post_list.append(root.value)

        return post_list


    def Max(self):
        
        list_values = self.pre_order()

        if len(list_values) == 0:
            return None
        
        max=list_values[0]
        
        for value in list_values:
            if value >= max :
                max = value
        return max
    




class BTS(Tree1):
    def __init__(self, value, ):
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
                self.left = BTS(num)
            else:
                self.left.add(num)
        else:
            if self.right is None:
                self.right = BTS(num)
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


# tree1 = Tree1()
# node1 = Tree_Node(5)
# tree1.root = node1

# node2 = Tree_Node(7)
# tree1.root.left = node2

# node3 = Tree_Node(9)
# tree1.root.right = node3

# node4 = Tree_Node(13)
# tree1.root.left.left = node4

# node5 = Tree_Node(20)
# tree1.root.left.right = node5

# node6 = Tree_Node(2)
# tree1.root.right.left = node6

# print(tree1.Max())