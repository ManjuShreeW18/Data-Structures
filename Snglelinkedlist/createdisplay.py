class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def Insert_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
    
        if self.head is None:
            print("empty")
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

l.Insert_beg(89)
l.Insert_beg(45)
l.display()





    