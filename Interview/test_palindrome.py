import pytest
from palindrome_LinkedList import *


def test_is_palindrome_true():
    # Test case for a palindrome linked list
    head = Node('t')
    head.next = Node('a')
    head.next.next = Node('c')
    head.next.next.next = Node('o')
    head.next.next.next.next = Node('c')
    head.next.next.next.next.next = Node('a')
    head.next.next.next.next.next.next = Node('t')
    assert is_palindrome(head) == True

    # Test case for another palindrome linked list
    head = Node('m')
    head.next = Node('o')
    head.next.next = Node('o')
    head.next.next.next = Node('m')
    assert is_palindrome(head) == True


def test_is_palindrome_false():
    # Test case for a non-palindrome linked list
    head = Node('h')
    head.next = Node('o')
    head.next.next = Node('u')
    head.next.next.next = Node('s')
    head.next.next.next.next = Node('e')
    assert is_palindrome(head) == False
