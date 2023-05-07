class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
   

    
    
    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    def insert(self, data):
        """Inserts a new node with that value before the first node of the list
        Args:
            value: value of the new node
            
            Returns: nothing
            
            Raises: nothing """
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def includes(self,data):
        """Indicates whether that value exists as a Node’s value somewhere within the list.
        Args:
            value: value of the new node
            
            Returns: Boolean
            
            Raises: nothing """
        current = self.head
        while current is not None:
            if current.value == data:
                return True
            current = current.next
        return False

    def to_string(self):
        """Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        Args:
            value: value of the new node
            
            Returns: string
            
            Raises: nothing """
        current = self.head
        string = ""
        while current is not None:
            string += f"{{ {current.value} }} -> "
            current = current.next
        string += "NULL"
        return string
    
    def insert_before(self, value, new_value):
        """
        Inserts a new node containing the given new_value before the first occurrence of the given value in the linked list.
        Parameters:
        ----------
        value : any
            The value to search for in the linked list.
        new_value : any
            The value to be stored in the new node.
        Returns:
        -------
        None
        """
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def insert_after(self, value, new_value):
        """
        Inserts a new node containing the given new_value after the first occurrence of the given value in the linked list.
        Parameters:
        ----------
        value : any
            The value to search for in the linked list.
        new_value : any
            The value to be stored in the new node.
        Returns:
        -------
        None
        """
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node:
            if current_node.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def delete(self, value):
        """
        Deletes the first node containing the given value from the linked list, if it exists.
        Parameters:
        ----------
        value : any
            The value to search for and delete from the linked list.
        Returns:
        -------
        None
        """
        current_node = self.head
        if current_node and current_node.value == value:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def kth_from_end(self, k):
        """
         Args:
            - k : The index of the node to return, where k = 1 returns the last node, k = 2 returns the second-last node, and so on.
        Returns:
            - The value of the kth node from the end of the linked list, or None if the linked list is empty, k is not a positive integer,
            or k is greater than or equal to the length of the linked list.
        """
        # Check if k is a positive and is an integer
        if type(k) != int or k <= 0:
            return None
        
         # Check if the linked list is empty
        if not self.head:
            return None

        # Calculate the length of the linked list
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        # Check if k is greater than or equal to the length of the linked lis
        if k >= length:
            return None
        
        # Traverse the linked list to find the kth node from the end
        current = self.head
        for i in range(length - k - 1):
            current = current.next

        return current.value
    # def kth_from_end(self, k):
    #     if k <= 0:
    #         return None

    #     # Get the length of the linked list
    #     length = 0
    #     current = self.head
    #     while current:
    #         length += 1
    #         current = current.next

    #     if k > length:
    #         return None

    #     # Calculate the position of the kth node from the beginning
    #     position = length - k

    #     # Traverse the linked list to find the kth node from the beginning
    #     current = self.head
    #     for i in range(position):
    #         current = current.next

    #     return current.value

    # def find_middle(self):
    #     if not self.head:
    #         return None

    #     slow = self.head
    #     fast = self.head

    #     # Traverse the linked list using two pointers,
    #     # one moving at half the speed of the other.
    #     # When the fast pointer reaches the end of the
    #     # list, the slow pointer will be at the middle node.
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next

    #     return slow.value

    
    
    

    # @staticmethod
    # def zipLists(list1:'LinkedList', list2:'LinkedList'):
    #     """
    #     Zips two linked lists together into one linked list, alternating between nodes from each list.
    #     Parameters:
    #     ----------
    #     list1 : LinkedList
    #         The first linked list to zip.
    #     list2 : LinkedList
    #         The second linked list to zip.
    #     Returns:
    #     -------
    #     LinkedList
    #         A new linked list containing the zipped nodes.
    #     """
        
        
    #     if list1.head is None:
    #         return list2
    #     if list2.head is None:
    #         return list1
    #     list1_current = list1.head
    #     list2_current = list2.head
    #     while list1_current and list2_current:
    #         list1_next = list1_current.next
    #         list2_next = list2_current.next
    #         list1_current.next = list2_current
    #         if list1_next is None:
    #             break
    #         list2_current.next = list1_next
    #         list1_current = list1_next
    #         list2_current = list2_next
    #     return list1

         
def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} -> '
                current = current.next
            
            output += " Null"
        return output  


