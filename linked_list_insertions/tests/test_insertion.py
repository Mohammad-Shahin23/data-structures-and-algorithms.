import pytest
from linked_list_insertions import LinkedList1

def test_append_single_node( ):
    linked_list = LinkedList1()
    linked_list.append(5)
    assert linked_list.head.value== 5

def test_append_multiple_nodes( ):
    linked_list = LinkedList1()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    assert linked_list.head.value== 5
    assert linked_list.head. next.value== 10
    assert linked_list.head. next. next.value== 15

def test_insert_before_middle_node( ):
    linked_list = LinkedList1()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.insert_before(10, 7)
    assert linked_list.head. next.value == 7
    assert linked_list.head. next. next.value == 10

def test_insert_before_first_node( ):
    linked_list = LinkedList1()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.insert_before(5, 2)
    assert linked_list.head.value ==  2
    assert linked_list.head. next.value == 5

def test_insert_after_middle_node( ):
    linked_list = LinkedList1()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.insert_after(10, 12)
    assert linked_list.head. next.value == 10
    assert linked_list.head. next. next.value == 12

def test_insert_after_last_node( ):
    linked_list = LinkedList1()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.insert_after(15, 17)
    assert linked_list.head. next. next. next.value== 17

