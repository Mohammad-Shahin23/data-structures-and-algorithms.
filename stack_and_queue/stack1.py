
from linked_list import Linkedlist

class Node:
    def __init__(self, value ):
        self.value = value
        self.next = None


class Stack1:
    def __init__ (self):
        self.Linkedlist = Linkedlist()
       

    def __str__(self):
        return str(self.Linkedlist)
    
   

    def isEmpty(self):
        """ this method will return the boolean true of the stack is empty
            and false if its not 
        """
        if self.Linkedlist.head is None:
            return True
        else:
            return False
        
    def push(self, value):
        """
            this method will add the value at the top of the stack by making a new nood 
            then coecting it to the head and the next value.
        """
        
        node = Node(value)
        node.next= self.Linkedlist.head 
        self.Linkedlist.head = node
    
    def pop(self):
        """
        this method will delet rhe first node in the linked list
        """
        if self.Linkedlist.head is None:
            raise IndexError("the list is empty!!")
        else:
            popValue =self.Linkedlist.head.value
            self.Linkedlist.head = self.Linkedlist.head.next
            return popValue
    def peek(self):
        """
        this method will return the first element in the linked list without removing it 

        """
        if self.Linkedlist.head is None:
            raise IndexError ("the stack is empty")
        else:
            headValue = self.Linkedlist.head.value
            return headValue
    
    def delete(self):
        """
        this method will delet the stack by changing the head value to null
        """
        self.Linkedlist.head = None


        