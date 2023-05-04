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
    class Queue:
        def __init__(self):
            self.front=None
            self.rear=None
        def enqueue(self,value):
            node = Node(value)
            if self.front is None:
                self.front = node
                self.rear=node
            else:
                self.rear.next = node
                self.rear = node
        def dequeue(self):
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
            if self.front is None:
                raise IndexError("This Queue is Empty!!!")
            else:
                return self.front.value
        def is_empty(self):
            return not bool(self.front)

    class Stack:
        def __init__(self):
            self.top = None
        def push(self, value):
            node = Node(value)
            if self.top == None:
                self.top = node
            else:
                node.next = self.top
                self.top = node
        def pop(self):
            if self.top == None:
                raise IndexError("This Stack is Empty!!!")
            else:
                temp = self.top
                self.top = self.top.next
                return temp.value
        def peek(self):
            if self.top == None:
                raise IndexError("This Stack is Empty!!!")
            else:
                return self.top.value
        def is_empty(self):
            return not bool(self.top)

