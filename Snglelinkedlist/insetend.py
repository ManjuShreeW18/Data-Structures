class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:

    def __init__(self):
        self.head=None

    def Insert_beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    # def Insert_end(self,data):
    #     ne=Node(data)
    #     if self.head is None:
    #         self.head=ne
    #     else:
    #         temp=self.head
    #         while temp.next:
    #             temp=temp.next
    #         temp.next=ne
    
    def Insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def Insert_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np


    def display(self):

        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
        print("none")

l=SLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3

l.Insert_beg(45)
l.Insert_beg(8)
l.Insert_end(78)
l.Insert_end(56)
l.Insert_pos(4,25)
l.Insert_pos(3,3)
l.display()