
from trees.Tree import Tree_Node, Tree1
from trees.tree_intersection import tree_intersection

tree = Tree1()
tree.root = Tree_Node(3)
tree.root.left = Tree_Node(2)
tree.root.right = Tree_Node(6)
tree.root.left.left = Tree_Node(13)
tree.root.left.right = Tree_Node(5)
tree.root.right.left = Tree_Node(20)
tree.root.right.right = Tree_Node(8)

tree2 = Tree1()
tree2.root = Tree_Node(9)
tree2.root.left = Tree_Node(2)
tree2.root.right = Tree_Node(17)
tree2.root.left.left = Tree_Node(20)
tree2.root.left.right = Tree_Node(5)
tree2.root.right.left = Tree_Node(18)

def test_tree_intersection():
    actual = tree_intersection(tree, tree2)
    actual.sort()
    expected = [2, 5, 20]
    expected.sort()
    assert actual == expected