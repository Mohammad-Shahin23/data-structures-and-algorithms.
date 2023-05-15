# Code Challenge Class-11: pseudo

The problem is to implement a queue data structure using two stacks in Python, where elements are added to one stack and removed from the other stack, using a first-in, first-out (FIFO) approach. The goal is to simulate the behavior of a queue using only stacks.

# White Bord Class-11: pseudo
![MarineGEO circle logo](/stack_and_queue/png/Screenshot%202023-05-08%20225721.png)







## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `enqueue` | O(1)        | O(n)             |
| `denqueue` | O(n)      | O(n)             |

## Solution
    class PseudoQueue:
    
    def __init__(self):
        """
        Initializes a PseudoQueue instance with an empty primary and secondary stack.
        """
        self.stackA = Stack1()
        self.stackB = Stack1()

    def __str__(self):
        return str(self.stackA.Linkedlist) + "\n" + str(self.stackB.Linkedlist)
        
    def enqueue(self, value):
        
        self.stackA.push(value)



            
    def dequeue(self):
       
        if self.stackA.isEmpty() and self.stackB.isEmpty():
            return("Queue is empty")
        if self.stackB.isEmpty():
            while not self.stackA.isEmpty():
                self.stackB.push(self.stackA.pop())

        return self.stackB.pop()
