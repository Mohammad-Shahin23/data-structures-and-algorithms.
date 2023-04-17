# import pytest

# from linked_list1.linked_list import LinkedList

# def test_instantiate_empty_linked_list():
#     linked_list = LinkedList()
#     expected = "NULL"
#     actual = linked_list.to_string()
#     assert actual == expected


# def test_insert_into_linked_list():
#     linked_list = LinkedList()
#     linked_list.insert("a")
#     expected = "{ a } -> NULL"
#     actual = linked_list.to_string()
#     assert actual == expected


# def test_head_property_points_to_first_node():
#     linked_list = LinkedList()
#     linked_list.insert("a")
#     linked_list.insert("b")
#     linked_list.insert("c")
#     expected = "c"
#     actual = linked_list.head.value
#     assert actual == expected


# def test_insert_multiple_nodes():
#     linked_list = LinkedList()
#     linked_list.insert("a")
#     linked_list.insert("b")
#     linked_list.insert("c")
#     expected = "{ c } -> { b } -> { a } -> NULL"
#     actual = linked_list.to_string()
#     assert actual == expected


# def test_return_true_when_finding_existing_value():
#     linked_list = LinkedList()
#     linked_list.insert("a")
#     linked_list.insert("b")
#     linked_list.insert("c")
#     expected = True
#     actual = linked_list.includes("b")
#     assert actual == expected


# def test_return_false_when_finding_nonexistent_value():
#     linked_list = LinkedList()
#     linked_list.insert("a")
#     linked_list.insert("b")
#     linked_list.insert("c")
#     expected = False
#     actual = linked_list.includes("d")
#     assert actual == expected


