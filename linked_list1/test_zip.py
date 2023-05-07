from linked_list import LinkedList

def test_zip_lists():
    # Test case 1 - zipping two empty linked lists should return an empty linked list
    list1 = LinkedList()
    list2 = LinkedList()
    result = list1.zip_lists(list1, list2)
    assert result.to_list() == []
def test_zip_lists2():
    # Test case 2 - zipping one empty linked list with a non-empty linked list should return the non-empty linked list
    list1 = LinkedList()
    list2 = LinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(3)
    result = list1.zip_lists(list1, list2)
    assert result.to_list() == [1, 2, 3]

def test_zip_lists3():
    # Test case 3 - zipping two linked lists with the same length should result in a new linked list with alternating nodes
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    list2.append(2)
    list2.append(4)
    list2.append(6)
    result = list1.zip_lists(list1, list2)
    assert result.to_list() == [1, 2, 3, 4, 5, 6]

def test_zip_lists4():
    # Test case 4 - zipping two linked lists with different lengths should result in a new linked list with all nodes from both lists
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    list2.append(3)
    list2.append(4)
    list2.append(5)
    result = list1.zip_lists(list1, list2)
    assert result.to_list() == [1, 3, 2, 4, 5]
