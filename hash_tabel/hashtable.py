from hash_tabel.linked_list import LinkedList

class HashTable():
    def __init__(self,size=3):
        self.size = size
        self.map = [None]*size

    def hash(self, key):
        """
        Hash an arbitrary key and return an integer.
        Args: 
            key: the key to be hashed
        Returns:    
            The hashed key.

        """
        sum_of_asccii = 0
        for ch in str(key):
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx
    
    def set(self, key, value):
        """
        Store the value with the given key.
        
        Args:
            key: the key to be hashed
            value: the value to be stored
        
        """
        hashed_key = self.hash(key)
        if not self.map[hashed_key]: # if the Bucket is empty
            self.map[hashed_key] = [key,value]
        else: # collision happeded
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key,value])
            else: # if the bucket contains one pair only
                chain = LinkedList()
                exsiting_pair = self.map[hashed_key]
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(exsiting_pair)
                chain.add(new_pair)
    
    def get(self, key):
        """ 
        Get the value associated with a key

        Args:
            key: the key to look for
        Returns:    
            The value associated with the key, or None if the key does not exist.
        """
        hash = self.hash(key)
        bucket = self.map[hash]
        if bucket is None:
            return None
        if isinstance(bucket, LinkedList):
            head = bucket.head
            while head:
                if head.data[0] == key:
                    return head.data[1]
                head = head.next
             
        else:
            if bucket[0] == key:
                return bucket[1]

    def has(self, key) :
        """
        Check if a key exists in the hashtable

        aregs:
            key: the key to look for
        Returns:
            True if the key exists, False otherwise
        """
        hash = self.hash(key)
        bucket = self.map[hash]
        if bucket is None:
            return False
        if isinstance(bucket, LinkedList):
            head = bucket.head
            while head:
                if head.data[0] == key:
                    return True
                head = head.next
            return False
            
        else:
            if bucket[0] == key:
                return True
            else:
                return False


    def keys(self):
        """
        Get all the keys in the hashtable
        aregs:
            key: the key to look for
        Returns:   
            A list of all the keys in the hashtable
        """
        keys = []
        for bucket in self.map:
            if isinstance(bucket, LinkedList):
                head = bucket.head
                while head:
                    keys.append(head.data[0])
                    head = head.next
            elif bucket:
                keys.append(bucket[0])

        return keys