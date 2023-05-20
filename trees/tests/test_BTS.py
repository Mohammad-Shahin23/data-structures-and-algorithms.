from Tree import BTS


def test_instantiate_empty_tree():
    tree = BTS(None)
    assert tree.value is None
    assert tree.left is None
    assert tree.right is None

def test_instantiate_tree_with_single_root():
    tree = BTS(5)
    assert tree.value == 5
    assert tree.left is None
    assert tree.right is None

def test_add_left_and_right_child_to_node():
    tree = BTS(5)
    tree.add(3)
    tree.add(7)
    assert tree.left.value == 3
    assert tree.right.value == 7


def test_contains_existing_node():
    tree = BTS(5)
    tree.add(3)
    tree.add(7)
    tree.add(4)
    tree.add(2)
    assert tree.contains(4) is True

def test_contains_non_existing_node():
    tree = BTS(5)
    tree.add(3)
    tree.add(7)
    tree.add(4)
    tree.add(2)
    assert tree.contains(6) is False


