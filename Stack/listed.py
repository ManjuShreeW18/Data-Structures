class Stack:
    def __init__(self):

        self.items=[]

    def push(self,data):
        if self.is_full():
            print("cant push the element",data)
        else:
            self.items.append(data)
            print(f"pushed element:{data}")

    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            removed=self.items.pop()
            print(f"popped element:{removed}")

    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(f"top element :{self.items[-1]}")

    def is_empty(self):
        return len(self.items)==0
    
    def is_full(self):
        return len(self.items)==self.items
    
    def recursive(self,n):
        if n==0:
            return 0
        print(n)
        return self.recursive(n-1)

    
    def display(self):
        print(f"stack:{self.items[::-1]}")

s=Stack()
s.push(2)
s.push(1)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.peek()

s.recursive(5)
s.display()