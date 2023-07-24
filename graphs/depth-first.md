# # Code Challenge Class-38: graph_business_trip
implement a depth-first traversal algorithm that starts from a given node (vertex) and explores all the nodes reachable from that node in a depth-first manner, visiting each node only once. The algorithm uses a stack to keep track of the nodes to be explored and a visited list to avoid visiting nodes multiple times.
# White Bord Class-Class-38: graph_business_trip
![MarineGEO circle logo](/graphs/png/Screenshot%202023-07-24%20231907.png)









## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `depth_first`  | O(n*e)    | O (n)           |




## Solution

  def depth_first(self, vertex):
        """
        This method returns a collection of nodes in the graph in depth-first order.
        param vertex: the node to start the traversal from
        returns: a collection of nodes in the graph in depth-first order
        """
        stack = [vertex]
        visited = [vertex]
        returnd = []
        
        while stack:
            m = stack.pop(0)
            returnd.append(m)
            for neighbour in self.adj_list[m]:
                if neighbour.vertex not in visited:
                    visited.append(neighbour.vertex)
                    stack.append(neighbour.vertex)
        return returnd