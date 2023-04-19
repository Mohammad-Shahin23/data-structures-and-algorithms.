class LinkedList:
    def __init__(self):
        self.head = None
        
    def kthFromEnd(self, k):
        if k < 0:
            return "Exception: k should be a positive integer."
        
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        
        if k >= length:
            return "Exception: k is greater than or equal to the length of the linked list."
        
        current = self.head
        for i in range(length - k - 1):
            current = current.next
        
        return current.value