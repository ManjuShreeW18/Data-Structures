class Stack:
    def __init__(self,size):
        self.items=[]
        self.size=size
        
    def push(self,data):
        if self.is_full():
            print("stack is full cant push",data)

        else:
            self.items.append(data)
            # print(f"pushed:{data}")

    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            popped=self.items.pop()
            print(f"popped:{popped}")

    def peek(self):
        if self.is_empty():
            print("stack is empty")

        else:
            print(f"peek element: {self.items[-1]}")
    
    def is_empty(self):
        return len(self.items)==0
    
    def is_full(self):
        return len(self.items)==self.items
    
    def display(self):
        print("Stack ",self.items[::-1])

s=Stack(10)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

s.display()

s.pop()
s.peek()       
s.is_empty()
s.is_full()
s.display() 