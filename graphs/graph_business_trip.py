from graph_cc35 import Graph

def price(graph, cities):
    """
        this method takes in a graph and a list of cities and returns the total cost of the trip
        param graph: the graph to check
        param cities: the list of cities to check
        returns: the total cost of the trip
    """
    total = 0
    path_exists = False
    for i in range(len(cities)-1):
        neighbors = graph.show_neighbors(cities[i])
        for neighbor in neighbors:
            if neighbor.vertex.value == cities[i+1].value:
                total += neighbor.weight
                path_exists = True
                break
            
        if not path_exists:
            return None
    return total

