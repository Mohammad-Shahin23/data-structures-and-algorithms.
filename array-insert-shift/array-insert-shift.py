def insertShiftArray(arr, val):
   
    if len(arr) % 2 == 0:
        mid = len(arr) // 2
    else:
        mid = (len(arr) - 1) // 2
    arr.insert(mid, val)
    return arr


arr1 = [2, 4, 6, -8]
val1 = 5
result1 = insertShiftArray(arr1, val1)
print(result1)  # Output: [2, 4, 5, 6, -8]

# Example 2
arr2 = [42, 8, 15, 23, 42]
val2 = 16
result2 = insertShiftArray(arr2, val2)
print(result2)  # Output: [42, 8, 15, 16, 23, 42]