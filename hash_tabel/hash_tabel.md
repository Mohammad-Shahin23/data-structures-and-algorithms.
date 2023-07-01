# Code Challenge Class-30: HashTabele
IThis is a Python implementation of a hash table data structure. A hash table is a data structure that allows efficient storage and retrieval of key-value pairs. It uses a hash function to map keys to indices in an underlying array, called the hash table.
# White Bord Class-17: HashTabele








## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `hash` | O(n)        | O (1)             |
| `set` | O(1) on average, but it can be O(n) in the worst case    | O(1)             |
| `get` | O(1) on average, but it can be O(n) in the worst case  | O (1)             |
| `has` | O(1) on average, but it can be O(n) in the worst case  | O (1)             |
| `hash`| O(n)        |  O(n)           |


## Solution

    class HashTable():
    def __init__(self,size=3):
        self.size = size
        self.map = [None]*size

    def hash(self, key):
       
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx
    
    def set(self, key, value):
       
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