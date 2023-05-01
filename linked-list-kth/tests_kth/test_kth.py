import pytest
from linked_list_kth import LinkedList, Node


def test_13(AA):
    expected= "Error : Your input can't be more than the length" 
    actual = AA.kthFromEnd(4)
    assert  expected == actual  
def test_14(AA):
    expected= "Error : Your input can't be more than the length" 
    actual = AA.kthFromEnd(7)
    assert  expected == actual  

def test_15():
    LL= LinkedList()
    LL.insert("A")
    assert LL.kthFromEnd(0) == "A"

def test_16(AA):
    expected= "C" 
    actual = AA.kthFromEnd(2)
    assert  expected == actual  
