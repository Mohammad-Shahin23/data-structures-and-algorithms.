
from hash_tabel.hashtable import HashTable



def tree_intersection(tree1, tree2):
    """
    This function takes two binary trees as an input and returns a list of the common values in both trees.
    args:
        tree1: a binary tree
        tree2: a binary tree
    Returns:
        a list of the common values in both trees
    """
    
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
  