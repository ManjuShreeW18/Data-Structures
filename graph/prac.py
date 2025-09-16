from collections import deque

class graph:
    def __init__(self,ver):
        self.ver=ver
        self.adj_list={i:[] for i in range(ver)}

    def add_edge(self,src,dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def Dfs(self,start):
        visited=[False] * self.ver
        stack=[start]

        while stack:
            top=stack.pop()
            print(top)
            
            for i in self.adj_list[top]:
                if not visited[i]:
                    visited[i]=True
                    stack.append(i)


    def display(self):
        for i in self.adj_list:
            print(f"{i} --> {self.adj_list[i]} ")

g1 = graph(5)           # Create graph with 5 vertices
g1.add_edge(0, 1)       # Add edge 0-1
g1.add_edge(0, 2)       # Add edge 0-2
g1.add_edge(1, 2)       # Add edge 1-2
g1.add_edge(3, 2)       # Add edge 3-2
g1.add_edge(1, 4)       # Add edge 1-4

print("\nDfs")
g1.Dfs(0)

print("\nGraph:")
g1.display()           