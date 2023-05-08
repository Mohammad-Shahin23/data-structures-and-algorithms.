from stack_and_queue.stack import Stack


class PseudoQueue:
    """
    This class implements the standard queue interface using two Stack instances.

    Attributes:
    stackA (Stack): first stack used to insert elements into the queue.
    stackB (Stack): second stack used to remove elements from the queue.
    """
    
    def __init__(self):
        """
        Initializes a PseudoQueue instance with an empty primary and secondary stack.
        """
        self.stackA = Stack()
        self.stackB = Stack()
        
    def enqueue(self, value):
        """
        Adds an element to the end of the queue using a first-in, first-out approach.
        """
        self.stackA.push(value)
        
    def dequeue(self):
        """
        Removes and returns the element at the front of the queue using a first-in, first-out approach.

        """
        if self.stackA.is_empty() and self.stackB.is_empty():
            return None
        
        if self.stackB.is_empty():
            while not self.stackA.is_empty():
                self.stackB.push(self.stackA.pop())
                
        return self.stackB.pop()
