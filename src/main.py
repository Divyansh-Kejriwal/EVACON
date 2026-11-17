from graph.graph import nodes, edges, Graph
from routing.dijkstra import dijkstra 

graph = Graph()

A = nodes(node_id = "A", node_type="room", population=2)
B = nodes(node_id = "B", node_type="corridor")
C = nodes(node_id = "C", node_type="corridor")
D = nodes(node_id = "D", node_type="room", population=16)
E = nodes(node_id = "E", node_type="corridor")
F = nodes(node_id = "F", node_type="room", population=13)
G = nodes(node_id = "G", node_type="corridor")
H = nodes(node_id = "H", node_type="room", population=6)
I = nodes(node_id = "I", node_type="corridor")
exit1 = nodes(node_id = "EA", node_type="room", population=10)
exit2 = nodes(node_id = "EB", node_type="room", population=12)

AB = edges(start=A, end=B, distance=12, width=13)
AC = edges(start=A, end=C, distance=12, width=13)
AE = edges(start=A, end=E, distance=12, width=13)
AF= edges(start=A, end=F, distance=12, width=13)
Fexit1 = edges(start=A, end=exit1, distance=12, width=13)
EF = edges(start=E, end=F, distance=12, width=13)
CD = edges(start=C, end=D, distance=12, width=13)
EH = edges(start=E, end=H, distance=12, width=13)
DH = edges(start=D, end=H, distance=12, width=13)
HI = edges(start=H, end=I, distance=12, width=13)
Iexit2 = edges(start=I, end=exit2, distance=12, width=13)
Gexit2 = edges(start=G, end=exit2, distance=12, width=13)

dijkstra(graph.adj, start=A, destination=exit1, speed=2)
dijkstra(graph.adj, start=F, destination=exit2, speed=2)
dijkstra(graph.adj, start=G, destination=exit2, speed=2)