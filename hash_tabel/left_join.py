

def left_join(hash_1, hash_2):
    """
    This function takes two hash tables and return a list of lists that contain the key, value from the first hash table and the value from the second hash table if the key exists in both hash tables.
    args:
        hash_1: the first hash table
        hash_2: the second hash table
        Returns:
            a list of lists that contain the key, value from the first hash table and the value from the second hash table if the key exists in both hash tables.
    """

    result = []
    for key in hash_1.keys():
        value = hash_1.get(key)

        result.append([key, value, hash_2.get(key)])

    
    
    return result

    

