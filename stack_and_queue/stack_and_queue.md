# Code Challenge Class-10: stack_and_queue

- The code defines two classes, Queue and Stack, that implement the behavior of a queue and a stack data structure respectively.
- enqueue: Adds a new node with a given value to the end of the queue. 
If the queue is empty, the front and rear pointers are set to the new node.
- dequeue: Removes the node at the front of the queue and returns its value. 
If the queue is empty, an IndexError is raised
- peek: Returns the value of the node at the front of the queue without removing it. 
If the queue is empty, an IndexError is raised
- push: Adds a new node with a given value to the top of the stack. 
If the stack is empty, the top pointer is set to the new node.
- pop: Removes the node at the top of the stack and returns its value. 
If the stack is empty, an IndexError is raised.
- is_empty: Returns True if the stack is empty and False otherwise.







## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `peek` | O(1)           | O(1)             |
| `push` | O(1)            | O(1)             |
| `pop` | O(1)         | O(1)             |
| `enqueue` | O(1)        | O(1)             |
| `denqueue` | O(1)        | O(1)             |

## Solution
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

