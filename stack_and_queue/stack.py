class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    """
    A simple implementation of a Stack using linked list.

    Stack:
    A data structure that stores a collection of elements, where elements are added and removed from the same end (top).
    """
    def __init__(self):
        """
          Initializes an empty Stack.
        """
        self.top = None

    def push(self, value):
        """ 
        Adds an element to the top of the Stack.
        """
        node = Node(value)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    def pop(self):
        """
          Removes and returns the top element of the Stack.
        """
        if self.top == None:
            raise IndexError("This Stack is Empty!!!")
        else:
            temp = self.top
            self.top = self.top.next
            return temp.value
    def peek(self):
        """ 
            Returns the value of the top element of the Stack without removing it.
        """
        if self.top == None:
            raise IndexError("This Stack is Empty!!!")
        else:
            return self.top.value
    def is_empty(self):
        """
            Checks if the Stack is empty
        """
        return not bool(self.top)
