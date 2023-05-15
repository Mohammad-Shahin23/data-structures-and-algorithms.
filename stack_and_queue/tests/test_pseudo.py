from pseudo import PseudoQueue





def test_pseudue1():
    pseudoA = PseudoQueue()
    

    pseudoA.enqueue(1)
    pseudoA.enqueue(2)
    pseudoA.enqueue(3)
    
    assert pseudoA.stackA.peek() == 3

def test_dequeue():
    pseudoA = PseudoQueue()
    pseudoB = PseudoQueue()

    pseudoA.enqueue(1)
    pseudoA.enqueue(2)
    pseudoA.enqueue(3)

    assert pseudoA.dequeue() == 1  # Check if the first enqueued element is dequeued

def test_dequeue_empty():
    pseudoA = PseudoQueue()
    pseudoB = PseudoQueue()

    assert pseudoB.dequeue() == "Queue is empty"  # Check if dequeuing from an empty queue returns the appropriate message

