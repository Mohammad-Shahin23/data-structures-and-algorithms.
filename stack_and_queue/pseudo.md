# Code Challenge Class-11: pseudo

The problem is to implement a queue data structure using two stacks in Python, where elements are added to one stack and removed from the other stack, using a first-in, first-out (FIFO) approach. The goal is to simulate the behavior of a queue using only stacks.
# White Bord Class-11: pseudo
![MarineGEO circle logo](/stack_and_queue/Screenshot%202023-05-08%20225721.png)







## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `enqueue` | O(1)        | O(n)             |
| `denqueue` | O(1)best and avarge O(0)worst        | O(n)             |

## Solution
    class PseudoQueue:
    
    def __init__(self):
     
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self, value):
       
    def dequeue(self):
        
        if self.stack1.is_empty() and self.stack2.is_empty():
            return None
        
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
                
        return self.stack2.pop()

