class Queue:
    def __init__(self,size):
        self.size=size
        self.items=[]
        self.front=-1
        self.rear=-1

    def is_empty(self):
        return self.front==-1
    
    def is_full(self):
        return self.rear==self.size-1 #self.size is index it means rear came to end
    
    def Enqueue(self,data):
        if self.is_full():
            print("Queue Overflow")
        else:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.items.append(data)
            print(f"Enqueued:{data}")

    def Dequeue(self):
        if self.is_empty():
            print("Queue Underflow")

        else:
            print(f"Dequeued:{self.items[self.front]}")
            self.front+=1
            if self.front > self.rear:
                self.front=self.rear=-1 #Empty queue
                self.items.clear()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(f"front element:{self.items[self.front]}") #we cant cpnfirm in 0 onlyfront ele wil be there so

    def display(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print("Queue: ",self.items[self.front:self.rear+1]) 
            #gives elements btw front and rear and +1 is to violate -1


q=Queue(10)
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Enqueue(50)
q.display()
q.Dequeue()    
q.peek()
q.display()