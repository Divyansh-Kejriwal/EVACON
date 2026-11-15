from graph.graph import Graph

def dijkstra(adjacecy, start, destination, speed):

    distances = {}
    previous = {}
    visited = []

    