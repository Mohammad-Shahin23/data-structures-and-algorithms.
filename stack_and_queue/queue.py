
from stack_and_queue.linked_list import Linkedlist

class Node:
    def __init__(self, value ):
        self.value = value
        self.next = None

class Queue1 :
    def __init__(self):
        self.linkedlist = Linkedlist()
    
    def __str__(self):
        return str(self.linkedlist)
    
        
    def isEmpty(self):
        """
            this method cheeks if the linked list is empty or not

        """
        if self.linkedlist.head is None:
            return True
        else:
            return False
    
        
    def enqueue(self, value):

        """
            this method adds a new node at the end of the linked list 
        """
        
        node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = node 
            self.linkedlist.tail = node
        else:
            self.linkedlist.tail.next = node
            self.linkedlist.tail = node

    def dequeue(self):
        """
            this method removes the first node from the begining of the linked list
        """

        if self.isEmpty() or self.linkedlist.head is None:
            raise IndexError("the queue is empty")
        else:
            tempNode = self.linkedlist.head.value
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail  = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return(tempNode)
        
    def peek(self):
        """
           this method returns the first element in the list
        """
        if  self.isEmpty() or self.linkedlist.head is None:
            raise IndexError("the queue is empty")
        else:
            return self.linkedlist.head.value
        