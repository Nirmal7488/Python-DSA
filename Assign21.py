class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Deque:
    def __init__(self,Start=None):
        self.Start=Start
    def is_empty(self):
        return self.Start==None
    def insert_front(self,data):
        if self.Start is not None:
            self.Start.prev=Node(None,data,self.Start)
            self.Start=self.Start.prev
        else:
            self.Start=Node(None,data,None)
    def insert_rear(self,data):
        if self.Start is not None:
            temp=self.Start
            while temp.next is not None:
                temp=temp.next
            temp.next=Node(temp,data,temp.next)
        else:
            self.Start=Node(None,data,None)
    def delete_front(self):
        if self.Start is not None:
            self.Start=self.Start.next
            self.Start.prev=None
        else:
            raise IndexError("Deque is Empty")
    def delete_rear(self):
        if self.Start is not None:
            temp=self.Start
            while temp.next is not None:
                temp=temp.next
            if temp.prev is not None:
                temp.prev.next=None
            else:
                self.Start=None
        else:
            raise IndexError("Deque is Empty")
    def get_front(self):
        if self.Start is not None:
            return self.Start.item
        else:
            raise IndexError("Deque is Empty")
    def get_rear(self):
        if self.Start is not None:
            temp=self.Start
            while temp.next is not None:
                temp=temp.next
            return temp.item
        else:
            raise IndexError("Deque is Empty")

d1=Deque()
d1.insert_front(8)
d1.insert_front(9)
d1.insert_front(2)
d1.insert_rear(7)
d1.insert_rear(5)
d1.delete_front()
d1.delete_rear()

print("Front :",d1.get_front())
print("Rear :",d1.get_rear())
