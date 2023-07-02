
from hashtable import HashTable
def repeated_word(string):
    """
    This function takes a long string as an input and returns the first repeated word in the string.
    args:
        string: a long string
    Returns:
        the first repeated word in the string
    """
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
