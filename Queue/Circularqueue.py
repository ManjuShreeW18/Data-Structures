class Circular:
    def __init__(self, size):
        self.size = size
        self.items = [None]*size  # elements should be none
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear+1) % self.size == self.front
    # front=0 rear=4 (for size 5)
    # (4+1) % 5 = 0 ==Front --> full

    def is_empty(self):
        return self.front == -1

    def Enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0  # insert first element
        self.rear = (self.rear+1) % self.size  # rear+1 % 5 =0 fpr circular
        self.items[self.rear] = data  # stores new data at new rear position
        print(f"Enqueued: {data}")

    def Dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        removed=self.items[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1) % self.size
        print(f"Dequeued:{removed}")

    def display(self):
        if self.is_empty():
            print("empty CQ")
            return
        i=self.front
        print("Queued elements:",end=" ")
        while True:
            print(self.items[i],end=" ")
            if i==self.rear:
                break
            i=(i+1) % self.size
        print()

q=Circular(10)
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Enqueue(50)
q.Enqueue(60)
q.display()

q.Dequeue()
q.Dequeue()
q.display()