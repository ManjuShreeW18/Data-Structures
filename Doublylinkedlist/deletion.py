class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None

    def Delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None #forward link destroyed
        self.head.prev=None #backward link destroyed

    def Delete_end(self):
        temp1=self.head.next # temp starts from the second node
        temp=self.head  # before starts from the head

        while temp1.next is not None:
            temp1=temp1.next
            temp=temp.next

        temp.next=None  #removes last link    (1.n,2.p)
        temp1.prev=None   # remove backward link from deleted node

    def Delete_pos(self,pos):
        temp=self.head.next
        before=self.head
        
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next

        before.next=temp.next
        temp.next=before
        temp.next=None
        temp.prev=None

    def search(self,value):
        temp=self.head
        pos=1 #searching starts from 1

        while temp:
            if temp.data == value:
                print("found at poition",pos)
                return
            temp=temp.next
            pos+=1
        print("not found")


    def display(self):
        temp=self.head
        if self.head is None:
            print("empty dll")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
            print("none")

l=DLL()
n1=Node(1)
l.head=n1
n2=Node(23)
n1.next=n2
n3=Node(21)
n2.next=n3
n4=Node(45)
n3.next=n4
n5=Node(50)
n4.next=n5
l.Delete_beg()
l.Delete_end()
l.Delete_pos(3)
l.search(21)
l.search(10)
l.display()


                

    