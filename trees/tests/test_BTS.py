from trees.Tree import BTS , Tree1 , Tree_Node


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


def test_max():
    tree1 = Tree1()
    node1 = Tree_Node(5)
    tree1.root = node1

    node2 = Tree_Node(7)
    tree1.root.left = node2

    node3 = Tree_Node(9)
    tree1.root.right = node3

    node4 = Tree_Node(13)
    tree1.root.left.left = node4

    node5 = Tree_Node(20)
    tree1.root.left.right = node5

    node6 = Tree_Node(2)
    tree1.root.right.left = node6
     
    assert tree1.Max() == 20

def test_max_empty():
    tree2 = Tree1()
    # print(tree2.pre_order(tree2.root))
    assert tree2.Max() == None
    