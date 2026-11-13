from graph.graph import nodes, edges, Graph

graph = Graph()

A = nodes(node_id="A", node_type="room", population=100)
B = nodes(node_id="B", node_type="intersection")
C = nodes(node_id="C", node_type="intersection")

e1 = nodes(node_id="exit1", node_type="exit")
e2 = nodes(node_id="exit2", node_type="exit")

AB = edges(start=A, end=B, distance=10, width=5)
BC = edges(start=B, end=C, distance=10, width=5)
Ae1 = edges(start=A, end=e1, distance=10, width=2.5)
Ce2 = edges(start=C, end=e2, distance=10, width=2.5)

graph.add_edge(AB)
graph.add_edge(BC)
graph.add_edge(Ae1)
graph.add_edge(Ce2)

graph.add_node(A)
graph.add_node(B)
graph.add_node(C)
graph.add_node(e1)
graph.add_node(e2)

graph.show_node_data("A")
graph.show_edge_data(0)