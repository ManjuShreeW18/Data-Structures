class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None

    def Insert_beg(self,data):
        nb=Node(data)
        nb.next=self.head  #forward link
        if self.head is not None:
            self.head.prev=nb  #backward link
        self.head=nb

    def Insert_end(self,data):
        ne=Node(data)
        temp=self.head #if u use if else remove this line else use it 
        # if self.head is None:   #if-else is optional
        #     self.head=ne
        # else:
        #     temp=self.head
        while temp.next:
            temp=temp.next
        temp.next= ne  # establishes connecton for forward link
        ne.prev=temp  #backward link

    def Insert_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
            np.prev=temp    
            np.next=temp.next
        if temp.next:
            temp.next.prev=np
            temp.next=np

    def display(self):
        temp=self.head
        if self.head is None:
            print("empty dll")
            return
        temp=self.head
        while temp:
            print(temp.data,"<-->",end=" ")
            temp=temp.next
        print("none")

    def Backward_display(self):
        temp=self.head
        if self.head is None:
            print("empty dll")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,"<-->",end=" ")
            temp=temp.prev
        print("None")
            
l=DLL()
n1=Node(1)
l.head=n1
n2=Node(23)
n1.next=n2
n2.prev=n1
n3=Node(21)
n2.next=n3
n3.prev=n2
n4=Node(45)
n4.prev=n3
n3.next=n4
l.Insert_beg(76)
l.Insert_end(6)
l.Insert_pos(3,80)
l.display()
l.Backward_display()

                

    