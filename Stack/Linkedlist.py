class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None  # Pointer to the top node

    def push(self, data):
        node = Node(data)
        node.next = self.top  # New node points to current top
        self.top = node       # Update top to new node
        print(f"pushed element: {data}")

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return
        removed = self.top.data
        self.top = self.top.next  # Remove top node
        print(f"popped element: {removed}")

    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return
        print(f"top element: {self.top.data}")

    def is_empty(self):
        return self.top is None

    def display(self):
        print("stack:", end=" ")
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def recursive(self, n):
        if n == 0:
            return
        print(n)
        self.recursive(n - 1)


# ---- Example Usage ----
stack = LinkedListStack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.pop()
stack.peek()

stack.recursive(3)

stack.display()
