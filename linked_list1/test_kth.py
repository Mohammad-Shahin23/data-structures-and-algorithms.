import pytest

from linked_list import LinkedList, Node

@pytest.fixture
def linked_list():
    # Create a sample linked list
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    return ll

def test_greater_than_list_length(linked_list):
    # Test case 1: k is greater than the length of the linked list
    assert linked_list.kth_from_end(5) is None

def test_ksame_as_list_length(linked_list):
    # Test case 2: k and the length of the list are the same
    assert linked_list.kth_from_end(4) is None

def test_not_positive_integer(linked_list):
    # Test case 3: k is not a positive integer
    assert linked_list.kth_from_end(-1) is None

def test_size_one():
    # Test case 4: the linked list is of a size 1
    ll = LinkedList()
    ll.append(1)
    assert ll.kth_from_end(1) is None

def test_happy_path(linked_list):
    # Test case 5: k is not at the end, but somewhere in the middle of the linked list
    assert linked_list.kth_from_end(2) == 3