from stack_and_queue.pseudo import PseudoQueue

def test_enqueue_single_element():
    queue = PseudoQueue()
    queue.enqueue(5)
    assert queue.stack1.stack == [5]
    assert queue.stack2.stack == []

def test_enqueue_multiple_elements():
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    assert queue.stack1.stack == [5, 10, 15]
    assert queue.stack2.stack == []

def test_dequeue_single_element():
    queue = PseudoQueue()
    queue.enqueue(5)
    assert queue.dequeue() == 5
    assert queue.stack1.stack == []
    assert queue.stack2.stack == []

def test_dequeue_multiple_elements():
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    assert queue.dequeue() == 5
    assert queue.dequeue() == 10
    assert queue.dequeue() == 15
    assert queue.stack1.stack == []
    assert queue.stack2.stack == []


