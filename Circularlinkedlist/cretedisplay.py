class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CLL:
    def __init__(self):
        self.head=None
        self.tail=None


    def display(self):
        if self.head is None:
            print("empty CLL")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next != self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data)
            

l=CLL()
n1=Node(1)

l.head=n1
l.tail=n1
l.tail.next=l.head # for empty CLL

n2=Node(2)
n1.next=n2
# l.tail.next=n2
# l.tail=n2
# l.tail.next=l.head

n3=Node(4)
n2.next=n3

n4=Node(5)
n3.next=n4

l.tail=n4
l.tail.next=l.head

l.display()
                

        

        