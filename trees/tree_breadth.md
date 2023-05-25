# Code Challenge Class-17: breadth
I need to make breadth-first traversal on a tree data structure. It aims to visit each node in the tree level by level, from left to right, and return a list of values in breadth-first order. The method uses a queue data structure to keep track of the nodes to be processed.
# White Bord Class-17: breadth
![MarineGEO circle logo](/trees/png/breath.png)







## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `_breadth_first` | O(n)        | O (n)             |
| `breadth` | O(n)      | O(n)             |

## Solution

    def breadth(self):
       
        arr = []
        return self._breadth_first(self.root, arr)

    def _breadth_first(self, root, breadth_list):
       
        if self.root is None:
            return breadth_list

        queue = [root]

        while queue:
            root = queue.pop(0)
            breadth_list.append(root.value)

            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)

        return breadth_list

