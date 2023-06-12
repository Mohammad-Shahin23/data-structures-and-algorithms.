def Insert(sorted, value):
    """
    Inserts a value into a sorted array while maintaining the sorted order.

    it takes two parameters:
    - sorted (list): The sorted array.
    - value (int): The value to be inserted.

    Returns None 
    """
    i = 0
    while i < len(sorted) and value > sorted[i]:
        i = i + 1
    sorted.insert(i, value)

def InsertionSort(input):
    """
    Sorts an input array using the insertion sort algorithm.

    input (list): The input array to be sorted.

    Returns a sorted (list): The sorted array.
    """
    sorted = [input[0]]
    for i in range(1, len(input)):
        Insert(sorted, input[i])
    return sorted
