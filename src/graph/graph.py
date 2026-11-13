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
        self.nodes_dict = {}
        self.edges_list = []

    def add_node(self, node):
        self.nodes_dict[node.id] = node

    def add_edge(self, edge):
        self.edges_list.append(edge) 

    def show_node_data(self, node_id):

        self.id = node_id
        get_node = self.nodes_dict.get(self.id)

        if get_node:
            print(f"The id of node is {get_node.id}")
            print(f"The type of node is {get_node.type}")
            print(f"The population of node is {get_node.population}\n")
        else:
            print("this node doesn't exist")

    def show_edge_data(self,edge_id):

        self.id = edge_id
        get_edge = self.edges_list[edge_id]
        
        if get_edge:
            print(f"The starting point of edge is {get_edge.start.id}")
            print(f"The eding point of edge is {get_edge.end.id}")
            print(f"The distance from start to end is {get_edge.distance} m")
            print(f"The width of edge is {get_edge.width} m\n")
        else:
            print("this edge doesn't exist")        
