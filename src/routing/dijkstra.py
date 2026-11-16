from graph.graph import Graph

def dijkstra(adjacecy, start, destination, speed):

    distances = {}
    previous = {}
    visited = []

    # Initial distances
    distances[start] = 0
    distances[destination] = float("inf")

    for i in adjacecy.keys():
        distances[i] = float("inf")

    # Processing the distances 

    while start != destination:
        visited.append(start)
        adjacent = adjacecy[start]

        for neighbour in adjacent:
            pass
        
               

    