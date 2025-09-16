

class graph:
    def __init__(self, ver):
        self.ver = ver
        # 4 ver means 4 falses created again loop executes
        self.adj_matrix = [[0] * ver for i in range(ver)]

    def add_edge(self, src, dest, weight):
        self.adj_matrix[src][dest] = weight
        self.adj_matrix[dest][src] = weight


    def display(self):
        for i in self.adj_matrix:
            print(i)


g1 = graph(4)
print("undirected graph")
g1.add_edge(0, 1, 20)
g1.add_edge(0, 2, 10)
g1.display()
