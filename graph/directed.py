class graph:
    def __init__(self,ver):
        self.ver=ver
        self.adj_matrix=[[False] * ver for _ in range(ver)]  # 4 ver means 4 falses created again loop executes

    def has_edge(self,src,dest):
        self.adj_matrix[src][dest]=True

    def display(self):
        for i in self.adj_matrix:
            print(i)

g1=graph(4)
print("directed graph")
g1.has_edge(0,1)
g1.has_edge(0,2)
g1.display()

# print("\ndirected graph")
# print(g1.has_edge(0,1))
# print(g1.has_edge(2,1))
# g1.display()