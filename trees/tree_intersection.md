# Code Challenge Class-31: HashTabele_repeted wards
IThis is a Python implementation of a hash table data structure. A hash table is a data structure that allows efficient storage and retrieval of key-value pairs. It uses a hash function to map keys to indices in an underlying array, called the hash table.
# White Bord Class-31: HashTabele_repeted wards
![MarineGEO circle logo](/hash_tabel/png/hashTable-repeted.png)








## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `set` | O(1) on average, but it can be O(n) in the worst case    | O(1)             |
| `has` | O(1) on average, but it can be O(n) in the worst case  | O (1)             |
| `tree_intersection`| O(n+m)        |   O(n+m)           |


## Solution

   def tree_intersection(tree1, tree2):
   
    hashTable = HashTable()
    common_values = []
    values_in_tree1 = tree1.pre_order()
    values_in_tree2 = tree2.pre_order()
    for value in values_in_tree1:
        hashTable.set(value, value)
    for value in values_in_tree2:
        if hashTable.has(value):
            common_values.append(value)
    return common_values
  