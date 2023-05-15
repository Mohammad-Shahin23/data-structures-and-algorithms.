class Linkedlist:
    def __init__ (self):
        self.head = None
        self.tail = None

    def __str__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output
    
    def __repr__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output

    def delete(self, value):
        

        temp = self.head

        # 1. Empty linked list
        if (temp is None):
            return False
        
        # 2. If the target is the first node
        if (temp is not None):
            if(temp.value == value):
                self.head = temp.next
                temp = None
                return value
            
        # search for the value and delete the target node
        while(temp is not None):
            if temp.value == value:
                break
            prev = temp
            temp = temp.next

        # 3. The value does not Exists
        if(temp is None):
            return False

        # unlinke the target node from the linkedlist
        prev.next = temp.next
        temp = None
        return value

