class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def Delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def Delete_end(self):
        temp=self.head
        prev=None #to break the connection
        while temp.next:
            prev=temp #temp is current node
            temp=temp.next
        prev.next=None #to delete last node

    def Delete_pos(self,pos):
        temp=self.head
        prev=None
        for i in range(pos-1):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp.next=None

    def search(self,value):
        temp=self.head
        pos=1

        while temp:
            if temp.data == value:
                print("found at position:",pos)
                return
            temp=temp.next
            pos+=1
        print("not found")


    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
            print("None")

l=SLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(5)
n3.next=n4
n5=Node(34)
n4.next=n5

l.Delete_beg()
l.Delete_end()
l.Delete_pos(2)
l.search(5)

l.display()        
        