class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CLL:
    def __init__(self):
        self.head=None
        self.tail=None  #add tail

    def Delete_beg(self):
        if self.head is None:
            print("empty CLL")
        else:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                temp=self.head
                self.head=temp.next  # Move head to next node
                self.tail.next=self.head
                
    def Delete_end(self):
        if self.head is None:
            print("empy CLL")
        else:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                temp=self.head

                while temp.next != self.tail:
                    temp=temp.next

                self.tail=temp  # Update tail
                self.tail.next=self.head

    # def Delete_pos(self,pos):
    #     if self.head is None:
    #         print("empty cll")

    #     elif pos==1:
    #         l.Delete_beg()
    #     else:
    #         temp1=self.head
    #         temp2=self.head
    #         for i in range(1,pos-1):
    #             temp1=temp1.next
    #             temp2=temp2.next

    #             temp1.next=temp2.next
    #             if temp2==self.tail:
    #                 self.tail=temp1
    #             temp2=None
    def Delete_pos(self, pos):
        if self.head is None:
            print("empty CLL") 
            
        elif pos == 1:
            self.Delete_beg()  # assumes this method exists
        else:
            temp = self.head
            for i in range(1,pos-1):
                temp = temp.next

            if temp.next==self.tail: #if we want to delete the last node 
                                      # we need to assign it to the prev node which is temp
                self.tail=temp  #assigned tail to the prev node before deleting it
            temp.next=temp.next.next #we hae 2 pointer the pos and the before node to disconnect
            


    def display(self):   #this is traversal code
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

n1=Node(10)
l.head=n1
l.tail=n1
l.tail.next=l.head

n2=Node(20)
n1.next=n2

n3=Node(30)
n2.next=n3

n4=Node(40)
n3.next=n4

n5=Node(50)
n4.next=n5

l.tail=n5
l.tail.next=l.head

l.Delete_beg()
l.Delete_end()
l.Delete_pos(3)
l.display()
