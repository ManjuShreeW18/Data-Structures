class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def Insert_beg(self,data):
        nb=Node(data)
        if self.head is None:
            self.head=self.tail=nb
            self.tail.next=self.head
        else:
            nb.next=self.head
            self.head=nb
            self.tail.next=self.head

    def Insert_end(self,data):
        ne=Node(data)
        if self.head is None:
            self.head=self.tail=ne
            self.tail.next=self.head
        else:
            self.tail.next=ne
            self.tail=ne
            self.tail.next=self.head

    def Insert_pos(self,pos,data):
        np=Node(data)
        if self.head is None:
            self.head=self.tail=np
            self.tail.next=self.head
        else:
            if pos==1:
                l.Insert_beg(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                np.next=temp.next
                temp.next=np

    def display(self):
        if self.head is None:
            print("empty CLL")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next != self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            # print(temp.next.data)
            print("(back to head)")
            

l=CLL()
l.Insert_beg(23)
l.Insert_beg(2)
l.Insert_beg(3)
l.Insert_beg(5)
l.Insert_beg(8)
l.Insert_beg(6)
l.Insert_end(32)
l.Insert_pos(2,34)

l.display()