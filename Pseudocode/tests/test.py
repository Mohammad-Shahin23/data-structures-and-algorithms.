import pytest
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
    

