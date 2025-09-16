class Deque:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size  # Fixed-size array
        self.front = -1  # Initially empty
        self.rear = -1

    def is_full(self):
        # Full if rear's next position is front
        # Example: front = 0, rear = 4 (size=5)
        # (4 + 1) % 5 = 0 == front → full
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def insert_rear(self, data):
        if self.is_full():
            print("Deque is full")
            return

        if self.is_empty():
            # First element
            self.front = self.rear = 0
        else:
            # Move rear forward in circular fashion
            # Example: rear = 4 → (4 + 1) % 5 = 0
            self.rear = (self.rear + 1) % self.size

        self.items[self.rear] = data
        print(f"Inserted at rear: {data}")

    def insert_front(self, data):
        if self.is_full():
            print("Deque is full")
            return

        if self.is_empty():
            # First element
            self.front = self.rear = 0
        else:
            # Move front backward in circular fashion
            # Example: front = 0 → (0 - 1 + 5) % 5 = 4
            self.front = (self.front - 1 + self.size) % self.size

        self.items[self.front] = data
        print(f"Inserted at front: {data}")

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty")
            return

        removed = self.items[self.front]

        if self.front == self.rear:
            # Only one element, now deque becomes empty
            self.front = self.rear = -1
        else:
            # Move front forward in circular fashion
            # Example: front = 4 → (4 + 1) % 5 = 0
            self.front = (self.front + 1) % self.size

        print(f"Deleted from front: {removed}")

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return

        removed = self.items[self.rear]

        if self.front == self.rear:
            # Only one element, now deque becomes empty
            self.front = self.rear = -1
        else:
            # Move rear backward in circular fashion
            # Example: rear = 0 → (0 - 1 + 5) % 5 = 4
            self.rear = (self.rear - 1 + self.size) % self.size

        print(f"Deleted from rear: {removed}")

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return

        print("Deque contents:", end=' ')
        i = self.front
        while True:
            print(self.items[i], end=' ')
            if i == self.rear:
                break
            i = (i + 1) % self.size  # Move to next index circularly
        print()

dq = Deque(5)

dq.insert_rear(10)     # rear = 0
dq.insert_front(5)     # front = 4 (circular back)
dq.insert_rear(15)     # rear = 1
dq.display()           # Output: 5 10 15

dq.delete_front()      # removes 5
dq.display()           # Output: 10 15

dq.delete_rear()       # removes 15
dq.display()           # Output: 10
