import pytest
from linked_list import LinkedList, Node


def test_1(AA):
    expected= "Error : Your input can't be more than the length" 
    actual = AA.kthFromEnd(4)
    assert  expected == actual  
def test_2(AA):
    expected= "Error : Your input can't be more than the length" 
    actual = AA.kthFromEnd(7)
    assert  expected == actual  

def test_3():
    LL= LinkedList()
    LL.insert("A")
    assert LL.kthFromEnd(0) == "A"

def test_4(AA):
    expected= "C" 
    actual = AA.kthFromEnd(2)
    assert  expected == actual  
