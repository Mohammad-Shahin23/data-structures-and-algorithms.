# Code Challenge Class-31: HashTabele_repeted wards
IThis is a Python implementation of a hash table data structure. A hash table is a data structure that allows efficient storage and retrieval of key-value pairs. It uses a hash function to map keys to indices in an underlying array, called the hash table.
# White Bord Class-31: HashTabele_repeted wards

![MarineGEO circle logo](/hash_tabel/png/hashTable-repeted.png)







## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `hash` | O(n)        | O (1)             |
| `set` | O(1) on average, but it can be O(n) in the worst case    | O(1)             |
| `has` | O(1) on average, but it can be O(n) in the worst case  | O (1)             |
| `repeated_word`| O(n)        |   O(n+k)           |


## Solution

   def repeated_word(string):
   
    list_of_words = []
    hashtable = HashTable()
    
    string = string.lower()
    string = string.replace(",", "")
    string = string.replace(".", "")
    
    
    list_of_words = string.split(" ")
    for word in list_of_words:
        if hashtable.has(word):
            return word
        else:
            hashtable.set(word, word)
    return None
