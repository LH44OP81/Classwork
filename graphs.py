class Graph:
    def __init__(self, directed = False):
        self.directed = directed
        self.adj_list = dict()
        pass
    def insert(self):
        pass
    def __repr__(self): #Dunder method
        graph_str = ""
        for node, neighbours in self.adj_list.items():
            graph_str += f"{node} -> {neighbours} \n"

        return graph_str

    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())

    def adj_matrix(self):
        nodes = self.get_nodes()

        index = {node: i for i, node in enumerate(nodes)}
        size = len(nodes)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for from_node, neighbors in self.adj_list.items():
            for to_node in neighbors:
                if isinstance(to_node, tuple):
                    to, weight = to_node
                    matrix[index[from_node]][index[to]] = weight
                else:
                    matrix[index[from_node]][index[to_node]] = 1

        return matrix

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already created")

    def add_edge(self, from_node, to_node, weight = None):

        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)

        else:
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def depth_first_search(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]

                    if neighbour not in visited:
                        stack.append(neighbour)
        return order
    def breadth_first_search(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:

            node = queue.pop(0)
            if node not in visited:

                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in neighbours:

                    if isinstance(neighbour, tuple):

                        neighbour = neighbour[0]
                    if neighbour not in visited:

                        queue.append(neighbour)
        return order



if __name__ == "__main__":
    graph_obj = Graph(directed= True)

    graph_obj.add_edge("A","B",2)
    graph_obj.add_edge("A","C",24)
    graph_obj.add_edge("B","D",50)

    print(graph_obj)
    print("DFS Search Yields: ", graph_obj.depth_first_search("A"))
    print("BFS Search Yields: ", graph_obj.breadth_first_search("A"))

    #print("DJIKSTRA: ", )
    #print("Shortest path first: ")