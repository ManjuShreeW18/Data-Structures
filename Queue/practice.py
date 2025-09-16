class Queue:
    def __init__(self,size):
        
        self.size=size
        self.items=[None]*size
        self.front=-1
        self.rear=-1

    def is_empty(self):
        return self.front==-1
    
    def is_full(self):
        return (self.rear+1)% self.size==self.front
        
    def Enqueue(self,data):
        if self.is_full():
            print("full")
            return
        
        
        if self.front==-1:
            self.front=0
        self.rear=(self.rear+1)% self.items
        self.items[self.rear]=data
        print(f"enqued:{data}")

    def Dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        removed=self.items[self.front]
        if self.front==self.rear:
            self.front=-1
        else:
            self.front=(self.front+1)%self.items
            print(f"dequed:{removed}")

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
            i=(i+1)%self.size
        print()









    

    




