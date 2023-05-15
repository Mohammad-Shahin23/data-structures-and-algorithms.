import pytest
from stack1 import Stack1
from queue1 import Queue1

def test_stack_push():
    stack = Stack1()
    stack.push(1)
    assert stack.peek() == 1

def test_stack_push_multiple():
    stack = Stack1()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_stack_pop():
    stack = Stack1()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_stack_empty():
    stack = Stack1()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.isEmpty()

def test_stack_peek():
    stack = Stack1()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.peek() == 3

def test_stack_instantiate_empty():
    stack = Stack1()
    assert stack.isEmpty()

def test_stack_pop_empty():
    stack = Stack1()
    with pytest.raises(IndexError):
        stack.pop()

def test_stack_peek_empty():
    stack = Stack1()
    with pytest.raises(IndexError):
        stack.peek()

def test_queue_enQueue1():
    queue = Queue1()
    queue.enqueue(1)
    assert queue.peek() == 1

def test_queue_enqueue_multiple():
    queue = Queue1()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

def test_queue_deQueue1():
    queue = Queue1()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3

def test_queue_peek():
    queue = Queue1()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1
    assert queue.peek() == 1

def test_queue_empty():
    queue = Queue1()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.isEmpty()

def test_queue_instantiate_empty():
    queue = Queue1()
    assert queue.isEmpty()

def test_queue_dequeue_empty():
    queue = Queue1()

    with pytest.raises(IndexError):
        queue.dequeue()

def test_queue_peek_empty():
    queue = Queue1()

    with pytest.raises(IndexError):
        queue.peek()