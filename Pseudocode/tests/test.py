import pytest
from merge_sort import merge_sort
from insertion import InsertionSort


def test_insertion_sort_unsorted():
    input_array = [8, 4, 23, 42, 16, 15]
    expected_output = [4, 8, 15, 16, 23, 42]
    sorted_array = InsertionSort(input_array)
    assert sorted_array == expected_output
    
def test_insertion_sort_sorted():
    input_array = [4, 8, 15, 16, 23, 42]
    expected_output = [4, 8, 15, 16, 23, 42]
    sorted_array = InsertionSort(input_array)
    assert sorted_array == expected_output
    

def test_insertion_sort_duplicates():
    input_array = [8, 4, 23, 42, 16, 15, 8, 15]
    expected_output = [4, 8, 8, 15, 15, 16, 23, 42]
    sorted_array = InsertionSort(input_array)
    assert sorted_array == expected_output
    
# ................................merge_sort.py...............................................


def test_random_array():
    arr = [8, 4, 23, 42, 16, 15]
    merge_sort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]

def test_reverse_sorted_array():
    arr = [20, 18, 12, 8, 5, -2]
    merge_sort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]

def test_array_with_few_uniques():
    arr = [5, 12, 7, 5, 5, 7]
    merge_sort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted_array():
    arr = [2, 3, 5, 7, 13, 11]
    merge_sort(arr)
    assert arr == [2, 3, 5, 7, 11, 13]

# # Run individual test cases
# test_random_array()
# test_reverse_sorted_array()
# test_array_with_few_uniques()
# test_nearly_sorted_array()
