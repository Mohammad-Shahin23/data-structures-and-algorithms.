import pytest
from linked_list_insertions.linked_list_insertions import LinkedList1





class TestLinkedList(pytest.TestCase):

    def test_append_single_node(self):
        linked_list = LinkedList1()
        linked_list.append(5)
        self.assertEqual(linked_list.head.value, 5)
    
    def test_append_multiple_nodes(self):
        linked_list = LinkedList1()
        linked_list.append(5)
        linked_list.append(10)
        linked_list.append(15)
        self.assertEqual(linked_list.head.value, 5)
        self.assertEqual(linked_list.head.next_node.value, 10)
        self.assertEqual(linked_list.head.next_node.next_node.value, 15)

    def test_insert_before_middle_node(self):
        linked_list = LinkedList1()
        linked_list.append(5)
        linked_list.append(10)
        linked_list.append(15)
        linked_list.insert_before(10, 7)
        self.assertEqual(linked_list.head.next_node.value, 7)
        self.assertEqual(linked_list.head.next_node.next_node.value, 10)

    def test_insert_before_first_node(self):
        linked_list = LinkedList1()
        linked_list.append(5)
        linked_list.append(10)
        linked_list.append(15)
        linked_list.insert_before(5, 2)
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.head.next_node.value, 5)

    def test_insert_after_middle_node(self):
        linked_list = LinkedList1()
        linked_list.append(5)
        linked_list.append(10)
        linked_list.append(15)
        linked_list.insert_after(10, 12)
        self.assertEqual(linked_list.head.next_node.value, 10)
        self.assertEqual(linked_list.head.next_node.next_node.value, 12)

    def test_insert_after_last_node(self):
        linked_list = LinkedList1()
        linked_list.append(5)
        linked_list.append(10)
        linked_list.append(15)
        linked_list.insert_after(15, 17)
        self.assertEqual(linked_list.head.next_node.next_node.next_node.value, 17)

if __name__ == '__main__':
    pytest.main()