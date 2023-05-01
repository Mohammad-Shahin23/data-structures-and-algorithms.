from linked_list import LinkedList, Node



def test_zipLists():
    # create two linked lists
    list1 = LinkedList()
    list1.insert(2)
    list1.insert(3)
    list1.insert(1)

    list2 = LinkedList()
    list2.insert(4)
    list2.insert(9)
    list2.insert(5)

    # zip the two linked lists
    zipped_list = LinkedList.zipLists(list1, list2)

    # check the result
    expected_output = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL"
    assert zipped_list.to_string() == expected_output

    # test with different lengths
    list1 = LinkedList()
    list1.insert(2)
    list1.insert(3)
    list1.insert(1)

    list2 = LinkedList()
    list2.insert(4)
    list2.insert(9)

    zipped_list = LinkedList.zipLists(list1, list2)
    expected_output = "{ 1 } -> { 4 } -> { 3 } -> { 9 } -> { 2 } -> NULL"
    assert zipped_list.to_string() == expected_output

    # test with empty lists
    list1 = LinkedList()
    list2 = LinkedList()

    zipped_list = LinkedList.zipLists(list1, list2)
    expected_output = "NULL"
    assert zipped_list.to_string() == expected_output

    # test with one empty list
    list1 = LinkedList()
    list1.insert(2)
    list1.insert(3)
    list1.insert(1)

    list2 = LinkedList()

    zipped_list = LinkedList.zipLists(list1, list2)
    expected_output = "{ 1 } -> { 3 } -> { 2 } -> NULL"
    assert zipped_list.to_string() == expected_output
