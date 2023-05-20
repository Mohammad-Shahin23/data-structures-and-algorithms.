# Code Challenge Class-15: BTS

A Binary Search Tree (BTS) is a hierarchical data structure.
It maintains an ordering property: elements in the left subtree are smaller or equal, and elements in the right subtree are greater.
Operations include insertion, searching, and deletion while preserving the ordering property.
Traversal allows visiting nodes in pre-order, in-order, or post-order.
# White Bord Class-15: BTS
![MarineGEO circle logo](/trees/png/BTS.png)







## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `add` | O(logn)        | O(1)             |
| `contains` | O(logn)      | O(1)             |

## Solution
    class BTS(Tree1):
    def __init__(self, value):
        """
        Initialize a BTS (Binary Search Tree) object with the given value.

        """
        super().__init__()
        self.value = value
        self.left = None
        self.right = None

    def add(self, num):
        """
        Add a node with the given value to the BTS.

        """
        if self.value is None:
            self.value = num
        elif num <= self.value:
            if self.left is None:
                self.left = BTS(num)
            else:
                self.left.add(num)
        else:
            if self.right is None:
                self.right = BTS(num)
            else:
                self.right.add(num)

    def contains(self, value):
        """
        Check if the BTS contains a node with the given value.


        Returns: A boolean indicating whether or not the value is present in the BTS.

        """
        if self.value == value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)