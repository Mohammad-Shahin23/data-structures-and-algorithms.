class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        """Initializes an empty Queue with front and rear set to None."""
        self.front=None
        self.rear=None
        
    def enqueue(self, value):
        """Adds an element to the rear end of the Queue.

        Args:
        - value: The value of the element to be added to the Queue.

        Returns: None
        """
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
            
    def dequeue(self):
        """Removes and returns an element from the front end of the Queue.

        Returns:
        - The value of the element that was removed from the front end of the Queue.

        Raises:
        - IndexError: If the Queue is empty.
        """
        if self.front is None:
            raise IndexError("This Queue is Empty!!!")
        if self.front == self.rear:
            temp = self.front
            self.front = None
            self.rear = None
            return temp.value
        else:
            temp = self.front
            self.front = self.front.next
            return temp.value
            
    def peek(self):
        """Returns the value of the element at the front end of the Queue without removing it.

        Returns:
        - The value of the element at the front end of the Queue.

        Raises:
        - IndexError: If the Queue is empty.
        """
        if self.front is None:
            raise IndexError("This Queue is Empty!!!")
        else:
            return self.front.value
            
    def is_empty(self):
        """Checks if the Queue is empty.

        Returns:
        - True if the Queue is empty, False otherwise.
        """
        return not bool(self.front)
