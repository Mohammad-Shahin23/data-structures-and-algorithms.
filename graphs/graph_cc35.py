from node import Node

class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        """
            this method initializes the graph
            self.adj_list: a dictionary of all the nodes in the graph
        """
        self.adj_list = {}

    def add_node(self, value):
        """
            this method adds a new node to the graph
            param value: the value of the new node
            returns: the new node
        """
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self,node1, node2, weight=0):
        """
            this method adds a new edge between two nodes in the graph
            param node1: the first node to connect
            param node2: the second node to connect
            param weight: the weight of the edge
            returns: nothing
        """

        if not node1 in self.adj_list.keys():
            return("this node does not exist")
        
        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)
        
    def show_vertices(self):
        """
            this method returns all of the nodes in the graph as a collection
            returns: a collection of all the nodes in the graph
        """
        return list (self.adj_list.keys())
    def show_neighbors(self, vertex):
        """
            this method returns a collection of edges connected to the given node
            param vertex: the node to get the neighbors from
            returns: a collection of edges connected to the given node
        """
        if self.adj_list[vertex] == []:
            return None
        else:

            return self.adj_list[vertex]
    
    def size(self):
        """ 
            this method returns the number of nodes in the graph
            returns: the number of nodes in the graph
        """
        if self.adj_list == {}:
            return "0"
        else:

            return len(self.adj_list.keys())
        
    def breadth_first(self, vertex):
         queue = []
         visited = [vertex] 
         returnd = []
         queue.append(vertex)
         while queue: 
             m = queue.pop(0)
             returnd.append(m)
              
             for neighbour in self.adj_list[m]: 
                 if neighbour.vertex not in visited:
                     visited.append(neighbour.vertex)
                     queue.append(neighbour.vertex)

         return returnd          
    

    # def __str__(self):
    #     output = ''
    #     for vertex in self.adj_list.keys():
    #         output += f'{vertex} -> '
    #         for edge in self.adj_list[vertex]:
    #             output += f'{edge.vertex} -----> '
    #         output += '\n'
    #     return output