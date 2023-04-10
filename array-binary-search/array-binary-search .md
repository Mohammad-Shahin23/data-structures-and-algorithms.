# Class 01
## made by mohammad Shahin


![MarineGEO circle logo](/array-binary-search/Screenshot%20(27).png)


# Approach & Efficiency
    time: O(log(n)) because it divide the array in half each while
    step space: O(1) because the variable we assign do not get effected by the array

# Solution
    def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1