from collections import deque  # Import deque for BFS queue

class graph:
    def __init__(self, ver):
        self.ver = ver                    # Number of vertices
        self.adj_list = {i: [] for i in range(ver)}  # Create adjacency list

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)  # Add dest to src list
        self.adj_list[dest].append(src)  # Add src to dest list (undirected)

    def bfs(self, start):
        visited = [False] * self.ver     # Track visited nodes - F F F F F
        queue = deque([start])            # Initialize queue with start 
        visited[start] = True             # 1st node is visited - T F F F F

        while queue:
            node = queue.popleft()        # Pop node from queue
            print(node, end=" ")          # Print current node

            for i in self.adj_list[node]:  # Iterate neighbors
                if not visited[i]:          # If neighbor not visited
                    visited[i] = True       # Mark visited
                    queue.append(i)         # Add to queue

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
            print(f"{i} → {self.adj_list[i]}")  # Print adjacency list

g1 = graph(5)           # Create graph with 5 vertices
g1.add_edge(0, 1)       # Add edge 0-1
g1.add_edge(0, 2)       # Add edge 0-2
g1.add_edge(1, 2)       # Add edge 1-2
g1.add_edge(3, 2)       # Add edge 3-2
g1.add_edge(1, 4)       # Add edge 1-4

print("BFS:")
g1.bfs(0)               # Run BFS starting at 0

print("\nGraph:")
g1.display()            # Display adjacency list

print("\nDfs")
g1.Dfs(0)

