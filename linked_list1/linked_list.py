class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        current = self.head
        result = ''
        while current is not None:
            result += f'{{ {current.value} }} -> '
            current = current.next
        result += 'NULL'
        return result
    
    if __name__ == '__main__':
      linked_list = LinkedList()

      linked_list.insert('A')
      linked_list.insert('B')
      linked_list.insert('C')
      # # linked_list.append('D')
      # # linked_list.append('E')
      linked_list.insert_after('A','f')
      
     
      
      print(linked_list)
      print(linked_list.count)

      print(linked_list.kthFromEnd(4))
      

    def zipLists(list1: 'LinkedList', list2: 'LinkedList') -> 'LinkedList':
        """
        Zips two linked lists together into one linked list, alternating between nodes from each list.
        Parameters:
        ----------
        list1 : LinkedList
            The first linked list to zip.
        list2 : LinkedList
            The second linked list to zip.
        Returns:
        -------
        LinkedList
            A new linked list containing the zipped nodes.
        """
        if not list1.head:
            return list2
        if not list2.head:
            return list1

        current1 = list1.head
        current2 = list2.head
        new_list = LinkedList()

        while current1 and current2:
            new_list.insert(current1.value)
            new_list.insert(current2.value)
            current1 = current1.next
            current2 = current2.next

        if current1:
            while current1:
                new_list.insert(current1.value)
                current1 = current1.next

        if current2:
            while current2:
                new_list.insert(current2.value)
                current2 = current2.next

        return new_list
