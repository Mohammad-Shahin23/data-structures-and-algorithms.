import pytest
from linked_list import LinkedList, Node


def test_zipLists1():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    linked_list2.append(4)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL"

def test_zipLists2():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    linked_list2.append(4)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NULL"

def test_zipLists3():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> NULL"

def test_zipLists_one_list_is_null():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 3 } -> { 2 } -> NULL"

def test_zipLists_both_lists_are_null():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "NULL"
