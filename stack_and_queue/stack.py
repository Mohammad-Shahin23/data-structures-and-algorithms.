class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    """
    A simple implementation of a Stack using a Python list.

    Stack:
    A data structure that stores a collection of elements, where elements are added and removed from the same end (top).
    """
    def __init__(self):
        """
          Initializes an empty Stack.
        """
        self.stack = []

    def push(self, value):
        """ 
        Adds an element to the top of the Stack.
        """
        self.stack.append(value)

    def pop(self):
        """
          Removes and returns the top element of the Stack.
        """
        if self.is_empty():
            raise IndexError("This Stack is Empty!!!")
        else:
            return self.stack.pop()

    def peek(self):
        """ 
            Returns the value of the top element of the Stack without removing it.
        """
        if self.is_empty():
            raise IndexError("This Stack is Empty!!!")
        else:
            return self.stack[-1]

    def is_empty(self):
        """
            Checks if the Stack is empty
        """
        return len(self.stack) == 0