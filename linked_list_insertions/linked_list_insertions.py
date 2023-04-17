class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList1:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            raise ValueError("List is empty")
        elif self.head.value == value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            raise ValueError("Node not found")

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            raise ValueError("List is empty")
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError("Node not found")

