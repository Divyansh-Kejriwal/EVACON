class nodes: 
    def __init__(self, node_id, node_type, population=0):
        self.id = node_id
        self.type = node_type
        self.population = population

class edges:
    def __init__(self, start, end, distance, width, uid = None):
        self.start = start
        self.end = end
        self.distance = distance
        self.width = width
        self.uid = uid

class Graph:
    def __init__(self):
        self.nodes_dict = {}
        self.edges_list = []
        self.adj = {}       ## for adjecny of nodes in outgoing direction and its a dict of list by node id

    def add_node(self, node):
        self.nodes_dict[node.id] = node

    def add_edge(self, edge):
        self.edges_list.append(edge)

        # For edge uid
        u = -1
        for i in self.edges_list:
            if i.start.id == edge.start.id and i.end.id == edge.end.id and edge.uid == None:
                u += 1
        edge.uid = f"{str(edge.start.id)}{str(edge.end.id)}{str(u)}"
        # For adjancy purpose

        if edge.start.id not in self.adj:
            outgoing_edges = []
            outgoing_edges.append(edge)
            node_outgoing = edge.start.id
            self.adj.update((node_outgoing,outgoing_edges))
        elif edge.start.id in self.adj.keys():
            self.adj[edge.start.id].append(edge)

    def show_node_data(self, node_id):

        get_node = self.nodes_dict.get(node_id)

        if get_node:
            print(f"The id of node is {get_node.id}")
            print(f"The type of node is {get_node.type}")
            print(f"The population of node is {get_node.population}\n")
        else:
            print("this node doesn't exist")

    def show_edge_data(self,edge_name):

        try:

            get_edge = self.edges_list[self.edges_list.index(edge_name)]
            print(f"The starting point of edge is {get_edge.start.id}")
            print(f"The eding point of edge is {get_edge.end.id}")
            print(f"The distance from start to end is {get_edge.distance} m")
            print(f"The width of edge is {get_edge.width} m\n")

        except:
            print("this edge doesn't exist")        
