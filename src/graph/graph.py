class nodes: 
    def __init__(self, node_id, node_type, population=0):
        self.id = node_id
        self.type = node_type
        self.population = population

class edges:
    def __init__(self, start, end, distance, width):
        self.start = start
        self.end = end
        self.distance = distance
        self.width = width

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_edge(self, edge):
        self.edges.append(edge) 

    def show(self):
        print(self.nodes)
        print(self.edges)