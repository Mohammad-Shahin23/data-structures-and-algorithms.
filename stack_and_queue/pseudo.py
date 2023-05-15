
from stack1 import Stack1


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
        self.stackA = Stack1()
        self.stackB = Stack1()

    def __str__(self):
        return str(self.stackA.Linkedlist) + "\n" + str(self.stackB.Linkedlist)
        
    def enqueue(self, value):
        """
        Adds an element to the end of the queue using a first-in, last-out approach.
        """
        self.stackA.push(value)



            
    def dequeue(self):
        """
        Add the remaining nodes to StackB
        Then Removes and returns the element at the front of the queue using a first-in, last-out approach.
        

        """
        if self.stackA.isEmpty() and self.stackB.isEmpty():
            return("Queue is empty")
        if self.stackB.isEmpty():
            while not self.stackA.isEmpty():
                self.stackB.push(self.stackA.pop())

        return self.stackB.pop()

        
       






        # if self.stackA.Linkedlist is None and self.stackB.Linkedlist is None:
        #     return None
        # else:
        #     tempNode = self.stackA.Linkedlist.head.value
        #     if self.stackA.Linkedlist.head == self.stackA.Linkedlist.tail:
        #         self.stackA.Linkedlist.head = None
        #         self.stackA.Linkedlist.tail  = None
        #     else:
        #         self.stackA.Linkedlist.head = self.stackA.Linkedlist.head.next
        #     # return(tempNode)
        
        # if self.stackA.Linkedlist != None and self.stackB.Linkedlist.isEmpty():
        #     while not self.stackA.Linkedlist is None:
        #          self.stackB.Linkedlist.push(tempNode)
        # return(tempNode)



        
        
        
        
        
        






        # if self.stackB.Linkedlist.isEmpty():
        #     while not self.stackA.Linkedlist.isEmpty():
        #         self.stackB.Linkedlist.enqueue(self.stackA.Linkedlist.dequeue)
                
        # return self.stackB.pop()
