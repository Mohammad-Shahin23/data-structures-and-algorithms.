from graph_cc35 import Graph

def test_add_node():
    graph1 = Graph()
    a = graph1.add_node("A")
    assert a.value == "A"

def test_add_edge():
    graph1 = Graph()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    graph1.add_edge(a,b)
    assert graph1.adj_list[a][0].vertex == b
    assert graph1.adj_list[b][0].vertex == a

def test_get_vertices():
    graph1 = Graph()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    print(graph1.show_vertices())
    assert graph1.show_vertices() == [a,b,c,d]

def test_get_neighbors():
    graph1 = Graph()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    print(graph1.show_neighbors(a))
    assert graph1.show_neighbors(a) == graph1.adj_list[a]
    assert graph1.show_neighbors(b) == graph1.adj_list[b]
    assert graph1.show_neighbors(c) == graph1.adj_list[c]
    assert graph1.show_neighbors(d) == graph1.adj_list[d]

def test_size():
    graph1 = Graph()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    assert graph1.size() == 4



def test_breadth_first():
    graph1 = Graph()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    print(graph1.breadth_first(a))
    assert graph1.breadth_first(a) == [a,b,c,d]
   
    

