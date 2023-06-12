# Insertion Sort
## Code Challenge 26

## Assignment
    Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.
    Once you are done with your article, code a working, tested implementation of Insertion Sort based on the pseudocode provided.

## pseudocode
    Insert(int[] sorted, int value)
    initialize i to 0
    WHILE value > sorted[i]
        set i to i + 1
    WHILE i < sorted.length
        set temp to sorted[i]
        set sorted[i] to value
        set value to temp
        set i to i + 1
    append value to sorted

    InsertionSort(int[] input)
    LET sorted = New Empty Array
    sorted[0] = input[0]
    FOR i from 1 up to input.length
        Insert(sorted, input[i])
    return sorted


# Blog Article:
Exploring Insertion Sort: A Step-by-Step Guide


- Insertion Sort is a simple sorting algorithm that works by repeatedly building a sorted portion of the array and inserting each unsorted element into its correct position within the sorted portion.
- In this article, we will review the provided pseudocode for Insertion Sort, trace the algorithm step-by-step using visual representations, and then implement the algorithm in code.
We will also examine the algorithm's behavior with various sample arrays.

## Python Code:

    def Insert(sorted, value):
   
        i = 0
        while i < len(sorted) and value > sorted[i]:
            i = i + 1
        sorted.insert(i, value)

    def InsertionSort(input):
        
        sorted = [input[0]]
        for i in range(1, len(input)):
            Insert(sorted, input[i])
        return sorted
    

## Step-by-Step Visualization
### sample array:
    [8, 4, 23, 42, 16, 15]

### Step 1:
- Initial state: [8]
Start with the first element in the sorted array.

### Step 2:
- [4, 8]
- Compare the second element (4) with the sorted array (8) and insert it at the correct position.

### Step 3:
- [4, 8, 23]
- Compare the third element (23) with the sorted array (4, 8) and insert it at the correct position.

### Step 4:
- [4, 8, 23, 42]
- Compare the fourth element (42) with the sorted array (4, 8, 23) and insert it at the correct position.

### Step 5:
- [4, 8, 16, 23, 42]
- Compare the fifth element (16) with the sorted array (4, 8, 23, 42) and insert it at the correct position.

### Step 6:
- [4, 8, 15, 16, 23, 42]
- Compare the sixth element (15) with the sorted array (4, 8, 16, 23, 42) and insert it at the correct position.

### The final sorted array is:
[4, 8, 15, 16, 23, 42].



## Conclusion:
This article explors into the Insertion Sort algorithm, examining its pseudocode and demonstrating its execution with visual aids. Furthermore, we translated the algorithm into code and validated its accuracy with a series of tests.

Insertion Sort proves to be a great algorithm when dealing with limited input sizes or arrays that are partially sorted.