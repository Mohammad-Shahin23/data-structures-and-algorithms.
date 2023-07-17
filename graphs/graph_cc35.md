# # Code Challenge Class-35: Graphs
This is a Python implementation of a Graph data structure. which  allows efficient storage and retrieval of key-value pairs, where the keys are called vertexes and the links are called edges. the key's value are the number of edges which are connected to the vertexs .
# White Bord Class-35: Graphs
![MarineGEO circle logo](/graphs/png/Graps-cc35.png)
# White Bord Class-36: Graphs BWS
![MarineGEO circle logo](/graphs/png/screenshot-bws.png)









## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `show_vertices`  | O(1)    | O (1)           |
| `show_neighbors` | O(n)    | O(1)            |
| `size`           | O(1)    | O (1)           |
| `breadth_first`  |  O(V + E)  | O (v)        |



## Solution

     def show_vertices(self):
       
        return self.adj_list.keys()
    
    def show_neighbors(self, vertex):
        
        if self.adj_list[vertex] == []:
            return None
        else:

            return self.adj_list[vertex]
    
    def size(self):
       
        if self.adj_list == {}:
            return "0"
        else:

            return len(self.adj_list.keys())
    