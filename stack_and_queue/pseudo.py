
from stack_and_queue.stack1 import Stack


class Node:
    def __init__(self, value ):
        self.value = value
        self.next = None


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

    def __str__(self):
        return str(self.stackA.Linkedlist)
        
    def enqueue(self, value):
        """
        Adds an element to the end of the queue using a first-in, first-out approach.
        """
        node = Node(value)

        
        
        if self.stackA.Linkedlist.head is None:
            self.stackA.Linkedlist.head = node 
            self.stackA.Linkedlist.tail = node
        else:
            self.stackA.Linkedlist.tail.next = node
            self.stackA.Linkedlist.tail = node
            
    # def dequeue(self):
    #     """
    #     Removes and returns the element at the front of the queue using a first-in, first-out approach.

    #     """
    #     if self.stackA.Linkedlist is None and self.stackB.Linkedlist is None:
    #         return None
    #     else:
    #         tempNode = self.stackA.Linkedlist.head.value
    #         if self.stackA.Linkedlist.head == self.stackA.Linkedlist.tail:
    #             self.stackA.Linkedlist.head = None
    #             self.stackA.Linkedlist.tail  = None
    #         else:
    #             self.stackA.Linkedlist.head = self.stackA.Linkedlist.head.next
    #         # return(tempNode)
        
    #     if self.stackA.Linkedlist != None and self.stackB.Linkedlist.isEmpty():
    #         while not self.stackA.Linkedlist is None:
    #              self.stackB.Linkedlist.push(tempNode)
    #     return(tempNode)



        
        
        
        
        
        






        # if self.stackB.Linkedlist.isEmpty():
        #     while not self.stackA.Linkedlist.isEmpty():
        #         self.stackB.Linkedlist.enqueue(self.stackA.Linkedlist.dequeue)
                
        # return self.stackB.pop()
